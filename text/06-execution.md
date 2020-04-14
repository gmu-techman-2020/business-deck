# Execution

Verkilo’s execution plan focuses on ensuring we can provide our services to our customer base when- and wherever they choose to write. We are using traditional agile  practices for development while we explore product-market best fit. We will maintain our infrastructure as code (IaC), to better manage change and re-constitute our entire ecosystem automatically. We will use private GitHub accounts for managing our code repository. Customer Service will leverage a moderated community approach as discussed in Customer Engagement, supra.

## Technology Solution / Product Development

**Summary.** We provide a multi-operating system application that supports literary work product creation and collaboration based on a JavaScript (JS) codebase. Several backend capabilities will leverage native Amazon Web Service (AWS) cloud functions that provide on-demand capabilities. Machine learning and performance analytics are provided through Amazon SageMaker using PyTorch and GraphQL as Software-as-a-Service (SaaS) within the AWS ecosystem of services.
Our service is comprised of eight, frontend and backend, initial components listed below. Each component provides value to the customer by providing a quality user experience and a one-stop interface for developing a creative project from any stage of the production process through to publication.

**Composer (Application Frontend).** The user interface (UI) is a cross-platform application written in Node.JS, leveraging React, Redux, and other related frameworks and libraries. The web application provides a single code base for the other platforms written entirely in JavaScript. We provide cross-platform support for mobile (specifically Android and iOS) devices via React Native. We provide desktop support via Electron. In addition, utilizing an integrated plugin to Microsoft Word will provide support to all the development spaces for authors and editors alike.

These various forms of UI provide a rich-text editor that can be used for composing, editing, and commenting on the book project, leveraging UTF-8 for multi-language support with multiple users able to collaborate in real time. Author/editor interactions are managed on platform, with active-push notifications. Editor-availability calendar is managed in the composer.

**Matchmaker (Application Frontend).** The “Matchmaker” component of the application suite offers a matching interface with profiles, reviews, scheduling and statistics akin to an Amazon marketplace crossed with a Match or Uber like interface. This service leverages predictive analytics (see section below) to help anticipate when an author needs to seek out an editor. It offers the author a set of editors identified by the audience and genre they edit for, the type of editing they provide, and their expected availability. This leverages AWS Lambda serverless Functions-as-a-Service (FaaS), docker containerization, and is written in a Python codebase.

**Data Store (Service Backend).** AWS AppSync will be used to implement GraphQL as a query language that will also our developers to write queries in an object structure over the standard text string. This will greatly reduce the complexity of legacy SQL queries between the front end and backend, which will mean lower direct costs to run API calls on AWS. As AppSync will be used as our API to handle requests from our users and retrieve appropriate data, AWS DynamoDB will be used to support the database services. DynamoDB is a serverless, NoSQL database service on AWS that will auto-scale on its own and will easily integrate with AppSync. To support the “Matchmaker” machine learning model, AWS Elastic Container Service (ECS) will be used as the compute resource for the integrated service offerings of Amazon SageMaker. This will ingest the analysis and supporting data for testing, training, testing, and bias/accuracy analysis to improve the machine learning algorithm. With ECS, we will be using Docker as the container image repository as it is already fully integrated into the ECS services. All customer proprietary data will be encrypted with 256-bit Advanced Encryption Standard (AES) symmetric encryption with private keys being managed through AWS Secrets Manager key-paired through a user-only access/egress account policy. This provides authors with a secure workspace for their projects while also allowing them granular access-control rights to the intellectual property to share with editors and the community at large.  This will be provided to the customer through a easy to use UI within the application frontend similar to sharing documents at different Read / Write levels in Google Docs.

**Importer (Service Backend).** This service converts uploaded RTF or DOCX file types into our proprietary format for storage. The process leverages Pandoc and Docker for processing. We virus-scan these uploaded documents as a part of our internal pipeline security. As a milestone event, we plan to implement and support a voice-to-text conversion of uploaded MP3/4 and WAV using AWS Transcribe to provide convenience for self-publishers to record thoughts and storytelling. Inherently, this will also assist visually impaired users with any difficulties they may otherwise encounter by self-publishing through standard means of writing and/or typing their work. Additional support for other services like Amazon Textract (Text-Recognition), Amazon Translate (Language Translation), and Amazon Polly (Text-to-Speech) so an authors and editors can dynamically work across all boundaries of the human senses.

**Exporter (Service Backend).** This service converts the stored work into publication-ready formats (PDF, EPUB, DOCX, RTF) and stores it on the author’s choice of local or cloud-based storage locations (i.e., Dropbox, iCloud, Google Drive, OneDrive, Box, S3). This conversion leverages Pandoc and LaTeX formatters processed using Lambda and Docker-based processing containers.[^exported-by-verkilo]

[^exported-by-verkilo]: Note: We used a prototype of Verkilo's Exporter to create the document you are now reading.

**Account Management (Security Backend).** User accounts will be managed by AWS Cognito, a service that provides identity management and access control to our application. Account creation, user/group management, MFA, device management, password policies, and more will be managed through this service to provide layered security and basic account management to our users. User permissions and user rights will be managed in conjunction with a secure enclave database and AWS Cognito groups. This will allow authors and editors to have transparently different permissions and access to the same resources depending on the role they are performing.

Cognito integrates with iOS, Android, Web, and desktop applications as is interconnects via application programming interface (API). Cognito will help the user to set these permissions based on their Verkilo subscription (time until expired, active/expired, etc.).

**Notification (Service Backend).** To automate notifications to our users, as well as to administrators on system-level events and monitoring, we will utilize the AWS Simple Notification Service (SNS) in combination with AWS’ Simple Email Service (SES). SNS/SES are easily integrated into many of the other services AWS offers, including Cognito. This will allow automated email and SMS messages to be sent to users for account-creation directions, self-management of credentials, and subscription related terms and annual renewals. These services will also assist in security event information management, automated incident response and recovery, and other logging/monitoring needs for security-related capabilities implemented into our platform.

**Predictive Analytics (Machine Learning Backend).** To start, the data collected from editors and authors will include their audience, genre, experience, and schedule as a few of the metrics which will serve as inputs for the machine learning models Verkilo intends to deploy.  These models will match characteristics of success through similarities and “chance of matching” between the authors and editors, which will serve as the iterative process of building a dynamic recommendation and offerings board for the “Matchmaker” service.
The data used to train the models will be derived from preexisting data collected from marketing outreach, known forums and sites through site-scraping web crawling and other data mining processes for an initial application of an algorithm for matching the two-sided relationships with iterative validations and assessments for bias and accuracy after Verkilo’s release through the use of real-time, production data. The initial data types used to train the “Matchmaker” will be a randomized at 80% of the collected data, and the test/validation data sets will comprise approximately 20% of the remainder. Our assumptions through research of best fit algorithms from what we know are the basis for Match.com, Tinder, and E-Harmony is to apply Hierarchical Agglomerative Clustering and K-Means Clustering models written in python to extract high-value relationships based on structured (known metrics) and unstructured data (unknown, derived variables). [@santos_dating_2020] Structured data types are metrics we have already predetermines through our research and unstructured data is collected from interactions between the author and editors and their use of the platform (i.e., blogs, media, and site-navigations).

We will use Amazon’s SageMaker Studio services to process over fifty (50) industry-leading, optimized, ML-based models utilizing the top three ML platforms (TensorFlow, PyTorch, and Apache MXNet), which are the industry preferred frameworks for text-based input, linear regression, reinforcement, and sentiment training. SageMaker Notebook, Experiment, and Debugger will be directly integrated into AWS’ machine learning services, which will allow quick implementation and delivery of our “Matchmaker” model and allow for a pipeline of additional data analytics and derivations of platform service metrics.

## Product Roadmap / Development Path

Verkilo leverages a platform business model by bringing two different market segments together. Our roadmap focuses on attracting both segments to the platform with the goal of generating revenue principally via the editor segment.

**Phase 1---Composer** involves building the composer capabilities and building out the infrastructure. During this phase, we will be focusing more on the author than the editor to start adding editable data to the platform. Early adopters will receive concierge scheduling by the team while we build out the automated matchmaking & scheduling.

**Phase 2---Matchmaker** involves delivering the automated matchmaking capability. We pilot the capability initially, replacing the concierge scheduling as we gain confidence in the automation's ability to schedule reliably.

**Phase 3---Scale** expands the offering to a larger audience.

**Phase 4---Exit** involves seeking acquisition by Amazon.

\newpage{}
## Key Activities

Verkilo will engage in the following key activities to derive value for our customers:

**Platform.** Verkilo's business model is dominated by its platform. Activities supporting the platform relate to its management, provisioning, and promotion.

**Author-Editor Coordinating.** Our key differentiator is our ability to match author and editor based on a series of professional and temporal criteria using machine learning and coordinating their schedules automatically. We will manage these proprietary capabilities as trade secrets and develop with a small core team.

**Product Development.** Verkilo is a cloud-based software product company. That is the core of what we do.

## Key Resources

**Platform.** Central to Verkilo's business model is its platform. This includes the storage, security, privacy, and resiliency of our customers' data, especially the work products produced by authors. Securely storing this information is as important to us as it is to the author.

**Physical.** Verkilo relies on no physical assets, with the core team working from home.

**Intellectual Property.** Verkilo is primarily a company focused on intellectual property.

- **Trademarks.** Verkilo is currently not trademarked according to the USPTO's TESS system. We will trademark Verkilo at the earliest opportunity.
- **Patents / Trade Secrets.** We view our matchmaking algorithm as a trade secret rather than something patentable. This position may shift after consulting with a patent attorney.

**Human.** Our core development team is key in developing our algorithm. While we start with part of the team offshore, we onshore the labor in favor of in-house developers as we gain our financial footing.


## Key Partners

Verkilo relies on the following key partners to provide our service to our customers:

**Amazon Web Services.** Verkilo uses a wide range of Amazon Web Services to develop and deliver our services to our customers.

**Adreno Technologies India Pvt. Ltd.** Adreno Technologies (India) Private Limited is one of the leading IT/ITES service providers in India, delivering IT & ITES Solutions to a diverse set of clients in more than 20 countries across the globe. We partner with Adreno to lower product-development costs to accelerate delivery to market.

**CLA LLP.** CLA is a professional services network and the eighth largest accountancy firm in the United States. CLA LLP provides our outsourced accounting support.
