#!/usr/bin/swift -F Carthage/Build/Mac/

// Tell Swift where to find sqlite & filekit framework.

import SQLite
import FileKit

let db = try Connection("olai.db")

let fileDirectory = Path.Current + "out"
var fileName = ""

for row in try db.prepare("SELECT * FROM entry") {
	// construct fileName; convert path & row value to string
	fileName = String(fileDirectory) + "/" + String(row[6]!) + ".md"

	// convert string to Path
	let postFile = TextFile(path: Path(fileName))

	try "Site: " + String(row[1]!) |> postFile 
	try "Title: " + String(row[9]!) |>> postFile
	try "Subtitle: " + String(row[7]!) |>> postFile
	try "Date: " + String(row[5]!) |>> postFile
	try "Slug: " + String(row[6]!) |>> postFile
	try "Tags: " + String(row[8]!) |>> postFile
	try "Type: " + String(row[4]!) |>> postFile
	try "Excerpt: " + String(row[3]!) |>> postFile
	try "---" |>> postFile
	try String(row[2]!) |>> postFile
}