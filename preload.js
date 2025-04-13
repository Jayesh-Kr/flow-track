const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  startTask: (taskName) => ipcRenderer.send('start-task', taskName),
  stopTask: () => ipcRenderer.send('stop-task'),
});
