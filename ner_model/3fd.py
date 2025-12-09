import json
import random

# 1. Define the specific Low-Level & Engineering Skills
skills= [
    # --- Programming Languages ---
    "Python", "Python 3", "CPython", "MicroPython", "CircuitPython", "Py",
    "C++", "CPP", "C Plus Plus", "Modern C++", "C++11", "C++14", "C++17", "C++20",
    "C", "Embedded C", "Objective-C", "Obj-C",
    "Java", "Java SE", "Java EE", "J2EE",
    "C#", "C Sharp", ".NET", ".NET Core", "ASP.NET", "ASP.NET Core", "Blazor",
    "JavaScript", "JS", "ES6", "ECMAScript", "TypeScript", "TS",
    "Go", "Golang",
    "Rust", "RustLang",
    "Swift", "SwiftUI",
    "Kotlin",
    "PHP", "PHP 7", "PHP 8",
    "Ruby", "Matlab", "Simulink",
    "R", "R Language", "RStudio",
    "Dart",
    "Scala",
    "Perl", "Lua", "Tcl",
    "Haskell", "Elixir", "Erlang", "Clojure", "Ocaml", "F#",
    "Assembly", "ASM", "x86 Assembly", "ARM Assembly", "MIPS",
    "Shell", "Bash", "Zsh", "PowerShell", "Scripting",
    "Fortran", "COBOL", "Pascal", "Ada", "Lisp", "Scheme", "Prolog",
    "VHDL", "Verilog", "SystemVerilog", "SystemC",

    # --- Web Development (Frontend & Backend) ---
    "HTML", "HTML5",
    "CSS", "CSS3", "SASS", "SCSS", "LESS", "Tailwind", "Tailwind CSS", "Bootstrap", "Material UI",
    "React", "React.js", "ReactJS", "Redux", "Redux Toolkit",
    "Next.js", "NextJS", "Gatsby",
    "Vue", "Vue.js", "VueJS", "Nuxt", "Nuxt.js", "Vuex",
    "Angular", "AngularJS", "Angular 2+", "RxJS",
    "Svelte", "SvelteKit",
    "Node", "Node.js", "NodeJS", "Express", "Express.js", "NestJS", "Fastify", "Koa",
    "Django", "Django REST Framework", "DRF",
    "Flask", "FastAPI", "Pyramid", "Tornado",
    "Spring", "Spring Boot", "Spring MVC", "Hibernate", "JPA",
    "Laravel", "Symfony", "CodeIgniter", "Yii", "CakePHP", "WordPress", "Drupal", "Magento",
    "Ruby on Rails", "Rails",
    "GraphQL", "Apollo",
    "REST", "RESTful API", "Web API", "gRPC", "WebSockets", "Socket.io",
    "JQuery", "AJAX", "JSON", "XML", "YAML",

    # --- AI, Machine Learning & Data Science ---
    "Artificial Intelligence", "AI",
    "Machine Learning", "ML", "Automl",
    "Deep Learning", "DL", "Neural Networks", "CNN", "RNN", "LSTM", "GAN",
    "Computer Vision", "CV", "OpenCV", "YOLO",
    "Natural Language Processing", "NLP", "NLTK", "Spacy", "Gensim",
    "LLM", "Large Language Models", "GPT", "BERT", "Transformers", "Hugging Face", "LangChain", "LlamaIndex",
    "Generative AI", "GenAI", "Stable Diffusion", "Midjourney",
    "Data Science", "Data Analytics", "Data Mining",
    "TensorFlow", "TF", "TFX",
    "PyTorch", "Torch",
    "Keras",
    "Scikit-learn", "Sklearn",
    "Pandas", "NumPy", "SciPy", "Matplotlib", "Seaborn", "Plotly",
    "Apache Spark", "Spark", "PySpark",
    "Hadoop", "HDFS", "MapReduce",
    "Kafka", "Apache Kafka",
    "Airflow", "Apache Airflow",
    "Tableau", "Power BI", "PowerBI", "Looker", "QlikView", "Qlik",
    "Big Data", "Data Engineering", "ETL", "Data Warehousing", "Snowflake", "Databricks",

    # --- Cloud Computing & DevOps ---
    "AWS", "Amazon Web Services", "EC2", "S3", "Lambda", "AWS Lambda", "CloudFormation", "RDS", "DynamoDB",
    "Azure", "Microsoft Azure", "Azure DevOps", "Azure Functions",
    "GCP", "Google Cloud", "Google Cloud Platform", "App Engine", "BigQuery",
    "Docker", "Docker Compose", "Containerization",
    "Kubernetes", "K8s", "Helm", "OpenShift", "Rancher",
    "Terraform", "IaC", "Infrastructure as Code",
    "Ansible", "Puppet", "Chef", "SaltStack",
    "Jenkins", "CircleCI", "Travis CI", "GitLab CI", "GitHub Actions", "Bamboo", "TeamCity",
    "Prometheus", "Grafana", "ELK", "ELK Stack", "Elastic Stack", "Splunk", "Datadog", "New Relic", "Nagios",
    "Nginx", "Apache HTTP Server", "HAProxy",
    "Linux Administration", "SysAdmin",
    "Serverless", "Microservices",

    # --- Cybersecurity ---
    "Cybersecurity", "Cyber Security", "InfoSec", "Information Security",
    "Network Security",
    "Penetration Testing", "Pen Testing", "Vulnerability Assessment", "VAPT",
    "Ethical Hacking", "CEH", "OSCP",
    "Cryptography", "Encryption", "PKI", "SSL", "TLS", "OpenSSL",
    "Firewall", "WAF", "IDS", "IPS",
    "SIEM", "SOC", "Splunk ES", "ArcSight", "QRadar",
    "Wireshark", "Nmap", "Metasploit", "Burp Suite", "Nessus", "Snort", "Tcpdump",
    "Malware Analysis", "Reverse Engineering", "Ghidra", "IDA Pro",
    "IAM", "Identity and Access Management", "Active Directory", "LDAP", "Okta", "Auth0", "OAuth", "SAML", "OIDC", "JWT",
    "AppSec", "Application Security", "OWASP", "OWASP Top 10",
    "Compliance", "GDPR", "HIPAA", "PCI-DSS", "ISO 27001", "NIST", "SOC2",
    "Forensics", "Digital Forensics",
    "Zero Trust", "Cloud Security", "DevSecOps",
    "Kali Linux", "Parrot Security",

    # --- Databases ---
    "SQL", "MySQL", "PostgreSQL", "Postgres",
    "Oracle", "Oracle DB", "PL/SQL",
    "SQL Server", "MSSQL", "T-SQL",
    "NoSQL",
    "MongoDB", "Mongo",
    "Cassandra", "Apache Cassandra",
    "Redis",
    "Elasticsearch",
    "DynamoDB",
    "Firestore", "Firebase Realtime Database",
    "Neo4j", "Graph Database",
    "CouchDB", "Couchbase",
    "MariaDB", "SQLite", "Realm",

    # --- Mobile Development ---
    "Android", "Android SDK", "Android Studio",
    "iOS", "iOS SDK", "Xcode", "Cocoa Touch",
    "React Native", "RN",
    "Flutter", "Dart",
    "Xamarin", "Maui", ".NET MAUI",
    "Ionic", "Cordova", "Capacitor",
    "Mobile App Development",

    # --- Tools, OS & Methodologies ---
    "Git", "GitHub", "GitLab", "Bitbucket", "Version Control", "SVN",
    "Linux", "Ubuntu", "Debian", "CentOS", "Red Hat", "RHEL", "Fedora", "Arch Linux", "Kali",
    "Unix",
    "Windows", "Windows Server",
    "MacOS",
    "Jira", "Confluence", "Trello", "Asana", "Monday.com",
    "Agile", "Scrum", "Kanban", "Waterfall", "SAFe", "SDLC",
    "CI/CD", "Continuous Integration", "Continuous Deployment",
    "Visual Studio", "VS Code", "VSC", "IntelliJ IDEA", "Eclipse", "PyCharm", "WebStorm",
    "Vim", "Neovim", "Emacs", "Nano",
    "Figma", "Adobe XD", "Sketch"
]

# 2. Define Templates to vary the sentence structure
# {skill} is the placeholder where the language will be inserted
templates = [
    "We are looking for a developer proficient in {skill}.",
    "Strong knowledge of {skill} is required for this embedded role.",
    "The candidate must have experience with {skill} programming.",
    "Our firmware is entirely written in {skill}.",
    "He has 5 years of experience in {skill} development.",
    "Experience in {skill} is a huge plus.",
    "The project involves writing low-latency code in {skill}.",
    "She optimized the legacy {skill} codebase.",
    "We need someone to debug {skill} modules.",
    "Can you write a compiler using {skill}?",
    "The hardware simulation was done using {skill}.",
    "Proficiency in {skill} and linear algebra is needed.",
    "The kernel module is implemented in {skill}.",
    "We are migrating our system from C to {skill}.",
    "Knowledge of hardware description languages like {skill} is essential.",
    "The algorithm requires a robust implementation in {skill}.",
    "This role focuses on {skill} for signal processing.",
    "You will be working with {skill} on a daily basis.",
    "The backend logic relies on high-performance {skill}.",
    "Understanding of memory management in {skill} is critical."
]

training_data = []

# 3. Generate 1000 samples
for _ in range(1000):
    skill = random.choice(skills)
    template = random.choice(templates)
    
    # Create the text
    text = template.format(skill=skill)
    
    # Calculate EXACT indices
    start_index = text.find(skill)
    end_index = start_index + len(skill)
    
    # Verify alignment (sanity check)
    if text[start_index:end_index] != skill:
        print(f"Error alignment for: {text}")
        continue

    # Construct spaCy format
    annotation = {
        "entities": [
            [start_index, end_index, "SKILL"]
        ]
    }
    
    training_data.append([text, annotation])

# 4. Save to file
with open("training_data.json", "w", encoding="utf-8") as f:
    json.dump(training_data, f, indent=2)

print(f"Successfully generated {len(training_data)} samples to 'training_data.json'")