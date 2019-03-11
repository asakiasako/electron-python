/**
 * Manage with stdio data received from child process.
 * You can rewrite these functions for your application.
 */

const childStdOut = (process.stdout)

const childStdErr = (process.stderr)

module.exports = {
  childStdOut,
  childStdErr
}
