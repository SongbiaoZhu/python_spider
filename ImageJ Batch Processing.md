# ImageJ Batch Processing

# Overview

A fundamental benefit to creating [scripts and macros](https://imagej.net/Scripting) in [ImageJ](https://imagej.net/ImageJ) is the ability to *reuse* their functionality *on more than one image*. Although this can be done manually, there are multiple ways to easily automate this batch processing. 

# General workflow

1.  Create a basic macro/script which operates on the active image or on a single file. 
   -  The [macro recorder](https://imagej.net/Introduction_into_Macro_Programming#The_recorder) is an excellent way to generate macro code.
   -  The [Introduction into Macro Programming](https://imagej.net/Introduction_into_Macro_Programming) explains the principles of macro writing.
2.  Apply your macro to a group of images. 
   -  These images do not need to be open in ImageJ already—they will be read in as part of the batch process.
   -  See below for details.

# Option 1 -  *Process  ▶  Batch  ▶  Macro...*

The fastest way to start batch conversion is via the [ *Process  ▶  Batch  ▶  Macro...*](http://imagej.net/docs/guide/146-29.html#toc-Subsubsection-29.12.3)  command. This will open a dialog (below) that will allow you to specify  an input and output directory. You can select an output file format,  and then use the `Add Macro Code` drop-down to generate a macro with the desired functionality. 

[![BatchProcess.png](https://imagej.net/_images/e/e8/BatchProcess.png)](https://imagej.net/File:BatchProcess.png)

# Option 2 - Script Template

Open the [script editor](https://imagej.net/Using_the_Script_Editor), select  *Templates  ▶  ImageJ 1.x  ▶  Batch  ▶  Process Folder (IJ1 Macro)*. This will generate the following boilerplate: 

[![Process folder ij1.png](https://imagej.net/_images/thumb/7/79/Process_folder_ij1.png/762px-Process_folder_ij1.png)](https://imagej.net/File:Process_folder_ij1.png)

Lines 26 and 27 can now be edited, replaced with the functional macro  code you would like to apply to all images of a given type in a folder.  Furthermore you can now modify the batch processing logic itself, for  example if you need to customize what (if any) output information is  saved. 

# Option 3 - Batch Processing with Script Parameters


 

| [![Information-sign.png](https://imagej.net/_images/thumb/2/24/Information-sign.png/40px-Information-sign.png)](https://imagej.net/File:Information-sign.png) | This section is currently being expanded to document the current state of the [SciJava Batch Processor](https://github.com/scijava/batch-processor/). The Batch Processor is a new addition to the SciJava/ImageJ framework. If you encounter any issues, please report/ask on the [forum](https://imagej.net/Forum). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |


 

# See also

-  [ *Process  ▶  Batch*](http://imagej.net/docs/guide/146-29.html#toc-Subsection-29.12) submenu.
-  [Scripting](https://imagej.net/Scripting) documentation and tutorials.
-  [How to apply a common operation to a complete directory](https://imagej.net/How_to_apply_a_common_operation_to_a_complete_directory)
-  [Assign your own keyboard shortcuts](https://imagej.net/Keyboard_shortcuts#Creating_your_own_keyboard_shortcuts)

 This page was last modified on 26 June 2018, at 15:35.