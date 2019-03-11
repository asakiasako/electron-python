const fs = require('fs')

if (!fs.existsSync('./py-app/.venv')) fs.mkdirSync('./py-app/.venv')
