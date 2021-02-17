# __Meme Generator__

**Version 1.0.0**

This is a web application that generates random memes. In this application when
user clicks on the `Random` button, a random meme is generated using an image
selected from a collection of images and using a quote selected from different
sources of file.

When user clicks on the `Creator` button, application lands user to a page
where user needs to enter the _Image_url_, _Quote_body_, and _Quote_author_.
This will create a new meme with given source of data.

---
## __Code Files/ Modules/ Directory - Structure__
Given code folder contains a `src` folder within it, which contains following
_files_, _modules_ and _directories_:

#### 1. _Data (directory)

This directory contains the application related data like DogQuotes, fonts,
 photos etc. We don't need to touch this to run this application. Although we
 can add more datasets later like we can add new quotes or images.

#### 2. Meme Engine (module)

The Meme Engine Module is responsible for manipulating and drawing text onto
 images. It contains _meme_engine.py_ script within it. We don't need to touch
 this to run this application

#### 3. Quote Engine (module)

The Quote Engine module is responsible for ingesting many types of files that
 contain quotes. It contains various scripts within it, which includes:
1. __ingestor_interface.py__ script - Abstract Interface class.
2. __csv_ingestor.py__ script - CSV Ingestor script which utilize the abstract
ingestor_interface as its base script. This is used to read .csv data.
3. __docx_ingestor.py__ script - DOCX Ingestor script which utilize the abstract
ingestor_interface as its base script. This is used to read .docx data.
4. __pdf_ingestor.py__ script - PDF Ingestor script which utilize the abstract
ingestor_interface as its base script. This is used to read .pdf data.
5. __text_ingestor.py__ script - TEXT Ingestor script which utilize the abstract
ingestor_interface as its base script. This is used to read .txt data.
6. __ingestor.py__ script - Ingestor script which is used to select the helper
ingestor class.
7. __quote_model.py__ script - class which encapsulates the quote's body and
author.

We don't need to touch this to run this application

#### 4. static (directory)

This directory will be used to save the memes which will be generated. We don't
 need to touch this to run this application.

#### 5. templates (directory)

This directory contains HTML templates which are used by flask framework to
create this application. We don't need to touch this to run this application.

#### 6. app.py (file)

Application script which will be used to run this application as web service.
We don't need to touch this to run this application.

#### 7. meme.py (file)

This will be used to run this app as command line tool. We don't need to
touch this to run this application.

#### 8. pdftotext.exe (tool)

This converter is required to convert pdf document to plain text document. This
will be required by the PDFIngestor class. This should be present in the `src`
folder.

#### 9. requirements.txt (file)

This file contains all the dependencies which needs to be installed, for this
application to work.

---

## __Prerequisites__

1. Install all the required dependencies as given in the `requirements.txt` file. Major libraries which needs to be installed are as
follows: flask, pandas, python -docx, pillow and requests.

2. Download and Install `XpdfReader` for your system, from: [https://www.xpdfreader.com/download.html](https://www.xpdfreader.com/download.html)

3. Download the Xpdf `command line tools`, from: [https://www.xpdfreader.com/download.html](https://www.xpdfreader.com/download.html)

4. Unzip the downloaded tools and copy paste the `pdftotext.exe` to the `src`
 folder. Note that this command line tool is already present in the `src`
 folder, but user can download and replace it, if given one is not compatible.

---

## __Application Execution__

1. Goto the `src` folder.
2. Right click inside the folder and open the Git Bash, using option: __Git Bash Here__
3. Run the application using the following command: __python app.py__
4. Goto Chrome and navigate to following url: [__https://localhost:5000__](https://localhost:5000)

---

## __Contributors__

- Aditya Rajput
