const electron = require('electron');
const {app, BrowserWindow, Tray, Menu, nativeImage, ipcMain} = electron;
const path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');
let loggerProcess = null;
let recordedData = [];
let activeTaskName = null;
let tray;
let win;

ipcMain.on('start-task', (event, taskName) => {
    if (loggerProcess) return;
  
    recordedData = [];
    activeTaskName = taskName;
    loggerProcess = spawn('python', ['logger.py']);
  
    loggerProcess.stdout.on('data', (data) => {
      const lines = data.toString().split('\n');
      lines.forEach(line => {
        if (line.trim()) {
          try {
            const parsed = JSON.parse(line);
            recordedData.push(parsed);
          } catch (e) {
            console.error('Invalid JSON from logger:', line);
          }
        }
      });
    });
  
    loggerProcess.stderr.on('data', (data) => {
      console.error(`Logger error: ${data}`);
    });
  
    loggerProcess.on('close', (code) => {
      console.log(`Logger exited with code ${code}`);
      loggerProcess = null;
  
      const filename = `${activeTaskName.replace(/\s+/g, '_')}_${Date.now()}.json`;
      fs.writeFileSync(filename, JSON.stringify(recordedData, null, 2));
      console.log(`Saved to ${filename}`);
    });
  
    console.log(`Started task: ${taskName}`);
  });
  
  ipcMain.on('stop-task', () => {
    if (loggerProcess) {
      loggerProcess.kill();
      console.log('Stopped task and saving data...');
    }
  });

const createWindow = () => {
    win = new BrowserWindow({
        height : 600,
        width : 800,
        webPreferences : {
            preload : path.join(__dirname, 'preload.js'),
            nodeIntegration: false,
            contextIsolation: true,
        }
    });

    win.on('close' ,(e) => {
        if(!app.isQuitting) {
            e.preventDefault();
            win.hide();
        } else {
            win = null;
        }
    })

    win.loadFile('index.html')
}

app.whenReady().then(()=>{


    const icon = nativeImage.createFromPath('download.png');
    tray = new Tray(icon);

    const contextMenu = Menu.buildFromTemplate([
        {
            label : "Start App",
            click : () => win.show()
        },
        {
            label : "Quit",
            click : () => {
                app.isQuitting = true;
                tray.destroy();
                app.quit();
            }
        }
    ])
    tray.setContextMenu(contextMenu);
    tray.setTitle("This app is for tracking");
    tray.setToolTip("Flow Track");
    createWindow();
    if(BrowserWindow.getAllWindows().length === 0) createWindow();
}).catch(()=>{
    console.log("Error while starting app");
});

app.on('window-all-closed' , ()=>{
    if(process.platform !== 'darwin') app.quit();
})