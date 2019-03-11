/**
 * Define Application Menu
 */
let template = [
  {
    label: 'Control',
    submenu: [
      {
        label: 'Nothing At All',
        click: function () {
          console.log('reserved')
        }
      }
    ]
  }
]

module.exports = template
