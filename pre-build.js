const fs = require('fs')

let jsonStr = fs.readFileSync('package.json')
let packageConfig = JSON.parse(jsonStr)

// === Add Build Version == //
packageConfig.version = packageConfig.version.replace(/-Build.*/, '')
packageConfig.version = `${packageConfig.version}-Build${((new Date().getTime() - 1546272000000) / 100).toFixed()}`
let modJsonStr = JSON.stringify(packageConfig, null, 2)
fs.writeFileSync('package.json', modJsonStr)

// === make nsh file ===
let nsTemplateStr = fs.readFileSync('build/installer.nsh.template', 'utf8')
let nsStr = nsTemplateStr.replace(/%productName%/g, packageConfig.build.productName)
fs.writeFileSync('build/installer.nsh', nsStr)
