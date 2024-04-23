#!/usr/bin/node
const fs = require('fs');
const file_name = process.argv[2];

fs.readFile(file_name, 'utf-8', (err, data) => {
	if (err)
	{
		console.log(err);
	}
	if (data)
	{
		console.log(data);
	}
})
