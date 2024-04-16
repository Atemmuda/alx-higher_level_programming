#!/usr/bin/node
/**
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found”
 */
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
