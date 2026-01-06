<div align="center">

  <a name="readme-top"></a>
  # Text Summarizer

  [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Completed-success)
  [![Technology](https://img.shields.io/badge/Technology-Python%20%7C%20Flask%20%7C%20SpaCy%20%7C%20NLTK-blueviolet)](https://github.com/Amey-Thakur/TEXT-SUMMARIZER)
  [![Research](https://img.shields.io/badge/Research-IJRASET-orange)](https://doi.org/10.22214/ijraset.2022.40066)
  [![Developed by Amey Thakur & Mega Satish](https://img.shields.io/badge/Developed%20by-Amey%20Thakur%20%26%20Mega%20Satish-blue)](https://github.com/Amey-Thakur/TEXT-SUMMARIZER)

  A robust web application leveraging multiple NLP algorithms (SpaCy, NLTK, Gensim, Sumy) to summarize textual content and URL sources, featuring a comparative analysis interface for evaluating summarization quality.

  **[Source Code](Source%20Code/)** &nbsp;&middot;&nbsp; **[Research Paper](https://doi.org/10.22214/ijraset.2022.40066)** &nbsp;&middot;&nbsp; **[Technical Specification](docs/SPECIFICATION.md)** &nbsp;&middot;&nbsp; **[Video Demo](https://youtu.be/2drrqsSB1Bc)**

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

  <table>
  <tr>
  <td align="center">
  <a href="https://github.com/Amey-Thakur">
  <img src="https://github.com/Amey-Thakur.png" width="150px;" alt="Amey Thakur"/><br />
  <sub><b>Amey Thakur</b></sub>
  </a>
  </td>
  <td align="center">
  <a href="https://github.com/msatmod">
  <img src="Mega/Mega.png" width="150px;" alt="Mega Satish"/><br />
  <sub><b>Mega Satish</b></sub>
  </a>
  </td>
  </tr>
  </table>

</div>

---

<!-- OVERVIEW -->
## Overview

This project implements a versatile **Text Summarizer** capable of condensing large bodies of text or web content into concise summaries. It serves as a comparative platform for various Extractive Summarization techniques, including frequency-based methods (SpaCy, NLTK) and graph-based algorithms (TextRank via Gensim, LexRank via Sumy).

Developed as a mini-project for the **8th Semester** curriculum, this system addresses the need for efficient information retrieval by automating the abstraction of key insights from documents. It features a Flask-based web interface that allows users to input raw text or URLs and visualize the comparative performance of different NLP models.

> [!IMPORTANT]
> **Research Impact**
>
> This project was published as a research paper in the **International Journal for Research in Applied Science and Engineering Technology (IJRASET)** (Volume 10, Issue 1) and is also available as a preprint on **viXra**.
>
> - [Preprint @viXra](https://vixra.org/abs/2202.0017)
> - [Published Paper @IJRASET](https://doi.org/10.22214/ijraset.2022.40066)
> - [Publication Certificate](https://github.com/Amey-Thakur/ACHIEVEMENTS/blob/main/Research%20Papers/Text%20Summarizer%20Using%20Julia/IJRASET40066%20-%20Text%20Summarizer%20Using%20Julia.pdf)

### Resources

| # | Resource | Description | Date | Link |
|---|---|---|---|---|
| 1 | **Source Code** | Full Python/Flask implementation | — | [View](Source%20Code/) |
| 2 | **Technical Report** | Comprehensive project report (PDF) | 2022 | [View](Mini-Project/TEXT%20SUMMARIZER.pdf) |
| 3 | **Presentation** | Project presentation slides (PPTX) | 2022 | [View](Mini-Project/TEXT%20SUMMARIZER.pptx) |
| 4 | **Research Article** | IJRASET Published Paper (Julia Implementation) | 2022 | [View](https://doi.org/10.22214/ijraset.2022.40066) |
| 5 | **Scholarly Preprint** | Formal research manuscript (viXra version) | 2022 | [View](https://vixra.org/abs/2202.0017) |
| 6 | **Publication Certificate** | Certificate of Publication (IJRASET) | 2022 | [View](https://github.com/Amey-Thakur/ACHIEVEMENTS/blob/main/Research%20Papers/Text%20Summarizer%20Using%20Julia/IJRASET40066%20-%20Text%20Summarizer%20Using%20Julia.pdf) |
| 7 | **Project Demo** | Real-time application walkthrough | — | [View](https://youtu.be/2drrqsSB1Bc) |

---

<!-- FEATURES -->
## Features

| Feature | Description |
|---------|-------------|
| **Multi-Algorithm Support** | Unified interface for SpaCy, NLTK, Gensim, and Sumy summarization engines. |
| **Comparative Analysis** | Side-by-side visualization of summaries with reading time reduction metrics. |
| **URL Scraper** | Integrated BeautifulSoup module to extract and process text directly from web links. |
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

```bash
TEXT-SUMMARIZER/
│
├── docs/                                          # Formal Documentation
│   └── SPECIFICATION.md                           # Technical Architecture & Spec
│
├── Mega/                                          # Archival Attribution Assets
│   ├── Filly.jpg                                  # Project-related Content Asset
│   └── Mega.png                                   # Author Profile Image (Mega Satish)
│   ...                                            # Additional Contextual Assets
│
├── Mini-Project/                                  # Research & Academic Assets
│   ├── TEXT SUMMARIZER.pdf                        # Technical Project Report
│   ├── TEXT SUMMARIZER.pptx                       # Project Presentation
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
├── LICENSE                                        # MIT License Terms
├── README.md                                      # Comprehensive Archival Entrance
└── SECURITY.md                                    # Vulnerability Exposure Policy
```

---

<!-- RESULTS GALLERY -->
## Results Gallery

### Application Interface
The interface provides a clean, side-by-side comparison of summarization results along with reading time metrics.

![Application Interface](https://user-images.githubusercontent.com/54937357/146636650-5e8909fe-0484-41b8-b1d9-03612cb34e70.png)

---

<!-- QUICK START -->
## Quick Start

### 1. Prerequisites
Ensure your environment meets the following requirements:
- **Python**: Version **3.6** or higher.
- **Packages**: Flask, SpaCy, NLTK, Gensim, Sumy.
- **NLP Models**: `en_core_web_sm` (SpaCy), `stopwords/punkt` (NLTK).

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
This project may serve as a practical example for courses in **Natural Language Processing**, **Web Development**, or **Artificial Intelligence**. It demonstrates the practical application of theoretical concepts like TextRank and LexRank.

**For Researchers**  
The comparative framework allows for the evaluation of different extractive summarization algorithms on custom datasets, providing a baseline for further research into abstractive methods.

---

<!-- LICENSE -->
## License

This repository and all linked academic content are made available under the **MIT License**. See the [LICENSE](LICENSE) file for complete terms.

> [!NOTE]
> **Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

Copyright © 2022 Amey Thakur & Mega Satish

---

<!-- ABOUT -->
## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur) & [Mega Satish](https://github.com/msatmod)  
**Academic Journey**: Bachelor of Engineering in Computer Engineering (2018-2022)  
**Institution**: [Terna Engineering College](https://ternaengg.ac.in/), Navi Mumbai  
**University**: [University of Mumbai](https://mu.ac.in/)

This project features the **Text Summarizer**, a utility developed as an **8th Semester Mini-Project**. It represents a culmination of studies in computational linguistics and software engineering, delivering a functional tool for automated text analysis.

**Connect**: [GitHub](https://github.com/Amey-Thakur) · [LinkedIn](https://www.linkedin.com/in/amey-thakur)

### Acknowledgments

Grateful acknowledgment to **[Mega Satish](https://github.com/msatmod)** for her collaborative excellence and technical contributions to this project. Her dedication to refining the NLP logic and user interface was instrumental in the project's success.

Special thanks to the Department of Computer Engineering at Terna Engineering College for providing the academic platform for this research.

---

<!-- FOOTER -->
<div align="center">

  [↑ Back to Top](#readme-top)

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#results-gallery) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

  <br>

  📝 **[Text Summarizer](https://github.com/Amey-Thakur/TEXT-SUMMARIZER)** &nbsp;·&nbsp; 🎓 **[Computer Engineering](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)**

  ---

  ### Presented as part of the 8th Semester Mini-Project @ Terna Engineering College

  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
