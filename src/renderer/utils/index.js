export const manageError = function (vm, err, callback) {
  vm.$alert(`[${err.name}] ${err.message}`, 'ERROR', {
    confirmButtonText: 'OK',
    type: 'error'
  })
  if (callback) {
    callback()
  }
}
