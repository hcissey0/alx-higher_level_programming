#!/usr/bin/node
import { argv } from 'node:process';
if (argv[2]) { console.log('Arguments found'); } else if (argv[1]) { console.log('Argument found'); } else { console.log('No argument'); }
