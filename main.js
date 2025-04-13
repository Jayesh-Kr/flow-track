const electron = require('electron');
const {app, BrowserWindow} = electron;

const createWindow = () => {
    const win = new BrowserWindow({
        height : 600,
        width : 800,
    })
}

app.whenReady().then(()=>{
    createWindow();
}).catch(()=>{
    console.log("Error while starting app");
})