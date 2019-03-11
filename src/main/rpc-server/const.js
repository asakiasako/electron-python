// select rpc-server port
const DEFAULT_SERVER_PORT = 23300
const PYTHON_PATH = process.env.NODE_ENV !== 'production' ? require('path').join(__pyAppPath, '.venv/Scripts/python.exe') : null
const PROCESS_PATH = process.env.NODE_ENV !== 'production' ? require('path').join(__pyAppPath, 'main.py') : require('path').join(__static, 'api', 'api.exe')

module.exports = {
  DEFAULT_SERVER_PORT,
  PYTHON_PATH,
  PROCESS_PATH
}
