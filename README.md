# DocGen

This tool was developed while following the class of Software Engineering (@UniPD).

The aim of this tool is to generate the documentation of test classes that uses the [structure]() reported.

The output is generated in HTML format.

## use
Execute it using 
```
python docGenerator.py
```
The script looks for all the files in the current folder and generates the HTML page

## structure
Create a comment using this structure above the test you want to document
```
/** 
* @title              title of the test
* @description        description of the test
* @expectedResults    result that you are expecting
* @actualResult       actual results of the test (may be different from the expected one)
* @dependencies       other tests
* @preConditions      conditions to call the test (ex. object is not null)
* @postConditions     conditions after the test has been called (ex. object has been modified)
*/
```
