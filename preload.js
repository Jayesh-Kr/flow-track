const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  startTask: (taskName) => ipcRenderer.send('start-task', taskName),
  stopTask: () => ipcRenderer.send('stop-task'),
  getTaskFiles: () => ipcRenderer.invoke('get-task-files'),
  replayTask: (filename) => ipcRenderer.send('replay-task', filename)
});
