
<div align="center">

  <a name="readme-top"></a>
  # Text Summarizer

  [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Completed-success)
  [![Technology](https://img.shields.io/badge/Technology-Python%20%7C%20Flask%20%7C%20SpaCy%20%7C%20NLTK-blueviolet)](https://github.com/Amey-Thakur/TEXT-SUMMARIZER)
  [![Developed by Amey Thakur & Mega Satish](https://img.shields.io/badge/Developed%20by-Amey%20Thakur%20%26%20Mega%20Satish-blue)](https://github.com/Amey-Thakur/TEXT-SUMMARIZER)

  A robust web application leveraging multiple NLP algorithms (SpaCy, NLTK, Gensim, Sumy) to summarize textual content and URL sources, featuring a comparative analysis interface for evaluating summarization quality.

  **[Source Code](Source%20Code/)** &nbsp;·&nbsp; **[Technical Specification](docs/SPECIFICATION.md)** &nbsp;·&nbsp; **[Video Demo](https://youtu.be/2drrqsSB1Bc)** &nbsp;·&nbsp; **[Live Demo](https://huggingface.co/spaces/ameythakur/text-summarizer)**

  [![Text Summarizer Demo](https://img.youtube.com/vi/2drrqsSB1Bc/0.jpg)](https://youtu.be/2drrqsSB1Bc)

</div>

---

<div align="center">

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#results-gallery) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

</div>

---

<!-- AUTHORS -->
<div align="center">

  ## Authors

  **Terna Engineering College | Computer Engineering | Batch of 2022**

  | <a href="https://github.com/Amey-Thakur"><img src="https://github.com/Amey-Thakur.png" width="150" height="150" alt="Amey Thakur"></a><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-green.svg)](https://orcid.org/0000-0001-5644-1575) | <a href="https://github.com/msatmod"><img src="https://raw.githubusercontent.com/Amey-Thakur/TEXT-SUMMARIZER/main/Mega/Mega.png" width="150" height="150" alt="Mega Satish"></a><br>[**Mega Satish**](https://github.com/msatmod)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--1844--9557-green.svg)](https://orcid.org/0000-0002-1844-9557) |
  | :---: | :---: |

</div>

> [!IMPORTANT]
> ### 🤝🏻 Special Acknowledgement
> *Special thanks to **[Mega Satish](https://github.com/msatmod)** for her meaningful contributions, guidance, and support that helped shape this work.*

---

<!-- OVERVIEW -->
## Overview

This project implements a versatile **Text Summarizer** capable of condensing large bodies of text or web content into concise summaries. It serves as a comparative platform for various Extractive Summarization techniques, including frequency-based methods (SpaCy, NLTK) and graph-based algorithms (TextRank via Gensim, LexRank via Sumy).

Developed as a mini-project for the **8th Semester** curriculum, this system addresses the need for efficient information retrieval by automating the abstraction of key insights from documents. It features a Flask-based web interface that allows users to input raw text or URLs and visualize the comparative performance of different NLP models.

> [!NOTE]
> **Research Impact & Certification**
>
> This project was published as a research paper in the **International Journal for Research in Applied Science and Engineering Technology (IJRASET)** (Volume 10, Issue 1) and is also available as a preprint on **viXra**. The project received an official **Publication Certificate** for its research contribution to natural language processing.
>
> - [Preprint @viXra](https://vixra.org/abs/2202.0017)
> - [Published Paper @IJRASET](https://doi.org/10.22214/ijraset.2022.40066)
> - [Publication Certificate](https://github.com/Amey-Thakur/ACHIEVEMENTS/blob/main/Research%20Papers/Text%20Summarizer%20Using%20Julia/IJRASET40066%20-%20Text%20Summarizer%20Using%20Julia.pdf)

### Resources

| # | Resource | Description |
|---|---|---|
| 1 | [**Technical Report**](Mini-Project/TEXT%20SUMMARIZER.pdf) | Detailed project documentation |
| 2 | [**Project Presentation**](Mini-Project/TEXT%20SUMMARIZER.pptx) | Visual demonstration and slides |
| 3 | [**Technical Specification**](docs/SPECIFICATION.md) | Technical Architecture & Specification |
| 4 | [**Source Code**](Source%20Code/) | Complete source code and documentation |
| 5 | [**Research Article**](https://doi.org/10.22214/ijraset.2022.40066) | IJRASET Published Paper |
| 6 | [**Scholarly Preprint**](https://vixra.org/abs/2202.0017) | Formal research manuscript (viXra) |
| 7 | [**Project Demo**](https://youtu.be/2drrqsSB1Bc) | Real-time demonstration of features |
| 8 | [**NLP Laboratory**](https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II) | Academic repository for NLP |

> [!TIP]
> **Algorithm Selection for Optimal Results**
>
> For long-form documents, **Gensim's TextRank** provides superior coherence by leveraging graph-based sentence ranking. For shorter texts or news articles, **SpaCy's frequency-based** approach offers faster execution with comparable quality.

---

<!-- FEATURES -->
## Features

| Feature | Description |
|---------|-------------|
| **Multi-Algorithm Support** | Unified interface for SpaCy, NLTK, Gensim, and Sumy summarization engines. |
| **Comparative Analysis** | Side-by-side visualization of summaries with reading time reduction metrics. |
| **Web Scraping** | Integrated BeautifulSoup module to extract and process text directly from web links. |
| **Material UI** | Responsive frontend built with Materialize CSS for a clean, modern research aesthetic. |
| **Performance Metrics** | Real-time calculation of original vs. summarized reading times and execution speed. |
| **Scholarly Codebase** | Fully documented source code with strict academic formatting and inline citations. |

### Tech Stack
- **Backend**: Python 3.x, Flask
- **NLP Libraries**: SpaCy, NLTK, Gensim, Sumy
- **Frontend**: HTML5, Materialize CSS, jQuery
- **Utilities**: BeautifulSoup4, lxml

---

<!-- PROJECT STRUCTURE -->
## Project Structure

```python
TEXT-SUMMARIZER/
│
├── docs/                                          # Formal Documentation
│   └── SPECIFICATION.md                           # Technical Architecture & Specification
│
├── Mega/                                          # Archival Attribution Assets
│   ├── Filly.jpg                                  # Project-related Content Asset
│   └── Mega.png                                   # Author Profile Image (Mega Satish)
│
├── Mini-Project/                                  # Research & Academic Assets
│   ├── TEXT SUMMARIZER.pdf                        # Technical Project Report (PDF)
│   ├── TEXT SUMMARIZER.pptx                       # Project Presentation (PPTX)
│   └── Text Summarizer Using Julia/               # Related Research Materials
│
├── Source Code/                                   # Application Implementation
│   ├── static/                                    # Frontend Assets (CSS/JS)
│   ├── templates/                                 # HTML Jinja2 Templates
│   ├── app.py                                     # Main Flask Application
│   ├── nltk_summarization.py                      # NLTK Logic Module
│   ├── spacy_summarization.py                     # SpaCy Logic Module
│   ├── spacy_summarizer.py                        # SpaCy Helper Module
│   ├── Procfile                                   # Heroku Deployment Config
│   └── requirements.txt                           # Dependency Manifest
│
├── .gitattributes                                 # Global Git LFS & Config
├── .gitignore                                     # Asset Exclusion Manifest
├── CITATION.cff                                   # Scholarly Citation Metadata
├── codemeta.json                                  # Software Metadata Manifest
├── LICENSE                                        # MIT License Terms
├── README.md                                      # Comprehensive Archival Entrance
└── SECURITY.md                                    # Vulnerability Exposure Policy
```

---

<!-- RESULTS GALLERY -->
## Results Gallery

### Application Interface
The interface provides a clean, side-by-side comparison of summarization results along with reading time metrics.

<div align="center">

![Application Interface](https://user-images.githubusercontent.com/54937357/146636650-5e8909fe-0484-41b8-b1d9-03612cb34e70.png)

</div>

---

<!-- QUICK START -->
## Quick Start

### 1. Prerequisites
Ensure your environment meets the following requirements:
- **Python**: Version **3.6** or higher.
- **Packages**: Flask, SpaCy, NLTK, Gensim, Sumy.
- **NLP Models**: `en_core_web_sm` (SpaCy), `stopwords/punkt` (NLTK).

> [!WARNING]
> **Technical Dependencies & Environment**
>
> This system requires **Python 3.6+** and multiple NLP libraries (SpaCy, NLTK, Gensim, Sumy). For stable execution, it is recommended to run this in an isolated virtual environment and ensure all SpaCy language models are downloaded prior to execution.

### 2. Setup & Installation
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Amey-Thakur/TEXT-SUMMARIZER.git
    cd TEXT-SUMMARIZER/Source\ Code
    ```
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

### 3. Launch Application
1.  **Run the Flask Server**:
    ```bash
    python app.py
    ```
2.  **Access the Interface**:
    -   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

<!-- USAGE GUIDELINES -->
## Usage Guidelines

This repository is openly shared to support learning and knowledge exchange across the academic community.

**For Students**  
Use this project as a reference for implementing NLP pipelines, understanding Flask web architecture, and integrating multiple machine learning libraries into a single application.

**For Educators**  
This project may serve as a practical example or supplementary teaching resource for **Natural Language Processing (`DLO8012`)** and **Computational Lab II (`CSL804`)** as part of the **8th Semester Computer Engineering** curriculum. Attribution is appreciated when utilizing content.

**For Researchers**  
The comparative framework allows for the evaluation of different extractive summarization algorithms on custom datasets, providing a baseline for further research into abstractive methods.

---

<!-- LICENSE -->
## License

This repository and all linked academic content are made available under the **MIT License**. See the [LICENSE](LICENSE) file for complete terms.

> [!NOTE]
> **Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

Copyright © 2022 Amey Thakur, Mega Satish

---

<!-- ABOUT -->
## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur) & [Mega Satish](https://github.com/msatmod)  
**Academic Journey**: Bachelor of Engineering in Computer Engineering (2018-2022)  
**Institution**: [Terna Engineering College](https://ternaengg.ac.in/), Navi Mumbai  
**University**: [University of Mumbai](https://mu.ac.in/)

This project features the **Text Summarizer**, a utility developed as an **8th Semester Mini-Project**. It represents a culmination of studies in computational linguistics and software engineering, delivering a functional tool for automated text analysis.

**Connect**: [GitHub](https://github.com/Amey-Thakur) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/amey-thakur) &nbsp;·&nbsp; [ORCID](https://orcid.org/0000-0001-5644-1575)

### Acknowledgments

Grateful acknowledgment to [**Mega Satish**](https://github.com/msatmod) for her exceptional collaboration and scholarly partnership during the development of this project. Her intellectual contributions, technical insights, and dedicated commitment to software quality were fundamental in achieving the system's analytical and functional objectives. Learning alongside her was a transformative experience; her thoughtful approach to problem-solving and encouragement turned challenges into meaningful learning moments. This work reflects the growth and insights gained from our side-by-side academic journey. Thank you, Mega, for everything you shared and taught along the way.

Grateful acknowledgment to the faculty members of the **Department of Computer Engineering** at Terna Engineering College for their guidance and instruction in Natural Language Processing. Their expertise in computational linguistics and algorithmic design helped shape the technical foundation of this project.

Special thanks to the mentors and peers whose encouragement, discussions, and support contributed meaningfully to this learning experience.

---

<div align="center">

  [↑ Back to Top](#readme-top)

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#results-gallery) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

  <br>

  🔬 **[Natural Language Processing Laboratory](https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II)** &nbsp;·&nbsp; 📝 **[Text Summarizer](https://github.com/Amey-Thakur/TEXT-SUMMARIZER)**

  ---

  #### Presented as part of the 8th Semester Mini-Project @ Terna Engineering College
  
  ---
  
  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
