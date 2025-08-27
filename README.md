# ScholarAI: An Autonomous Agent for Scientific Literature Review and Synthesis

This project is an autonomous agent that receives a research topic, finds the 3-5 most relevant academic articles, reads their PDFs, and generates a summary report in Markdown format.

## System Architecture
![Diagram of System Architecture](docs/Architecture.png)

## Specifications
For a detailed description of the input, expected output format, and functional requirements, please refer to the [Detailed Specifications Document](docs/SPECIFICATIONS.md).

## Testing
First testing session: tools.py

Found 3 papers in arXiv about 'transformer models'.
--- Article 1 ---
Title: Model Validation in Ontology Based Transformations
Authors: Jesús M. Almendros-Jiménez, Luis Iribarne
URL of PDF: http://arxiv.org/pdf/1210.6111v1

--- Article 2 ---
Title: A Mathematical Model, Implementation and Study of a Swarm System
Authors: Blesson Varghese, Gerard McKee
URL of PDF: http://arxiv.org/pdf/1310.2279v1

--- Article 3 ---
Title: Towards Lightweight Transformer via Group-wise Transformation for Vision-and-Language Tasks
Authors: Gen Luo, Yiyi Zhou, Xiaoshuai Sun, Yan Wang, Liujuan Cao, Yongjian Wu, Feiyue Huang, Rongrong Ji
URL of PDF: http://arxiv.org/pdf/2204.07780v1


Second testing session: parser.py

Found 3 papers in arXiv about 'transformer models'.

--- Processing Article 1: Model Validation in Ontology Based Transformations ---
Uploading the PDF: http://arxiv.org/pdf/1210.6111v1...
Download finished. Extracting text...
Text extraction concluded.

--- Sample of extracted text (first 500 car.) ---
J. Silva and and F. Tiezzi (Eds.): Workshop on Automated Speciﬁcation and Veriﬁcation of Web Systems (WWV 2012) EPTCS 98, 2012, pp. 17–30, doi:10.4204/EPTCS.98.4 c⃝Jess´us M. Almendros-Jim´enez & Luis Iribarne This work is licensed under the Creative Commons Attribution License. Model Validation in Ontology Based Transformations∗ Jes´us M. Almendros-Jim´enez jalmen@ual.es Dpto. de Lenguajes y Computaci´on Universidad de Almer´ıa 04120-Spain Luis Iribarne luis.iribarne@ual.es Dpto. de Lenguajes y .


Thirth testing session: All together (Integrated Pipeline)

Found 3 papers in arXiv about 'transformers models'.

--- Processing article 1/3: Model Validation in Ontology Based Transformations ---
Uploading the PDF: http://arxiv.org/pdf/1210.6111v1...
Download finished. Extracting text...
Text extraction concluded.
Text from the article saved at: data\Model Validation in Ontology Based Transformations.txt

--- Processing article 2/3: A Mathematical Model, Implementation and Study of a Swarm System ---
Uploading the PDF: http://arxiv.org/pdf/1310.2279v1...
Download finished. Extracting text...
Text extraction concluded.
Text from the article saved at: data\A Mathematical Model Implementation and Study of a Swarm System.txt

--- Processing article 3/3: Towards Lightweight Transformer via Group-wise Transformation for Vision-and-Language Tasks ---
Uploading the PDF: http://arxiv.org/pdf/2204.07780v1...
Download finished. Extracting text...
Text extraction concluded.
Text from the article saved at: data\Towards Lightweight Transformer via Groupwise Transformation for VisionandLanguage Tasks.txt


Fourth testing session: Executor.py