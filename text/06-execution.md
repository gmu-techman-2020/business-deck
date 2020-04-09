# Execution

Verkilo's execution plan focuses on ensuring we can provide our services to our customer base when- and wherever they choose to write. We are using traditional agile for development while we explore product-market fit. We will maintain our infrastructure as code (IaC), allowing us to better manage change and re-constitute our entire ecosystem automatically. We will use GitHub for managing our code repository. Customer Service will leverage a moderated community approach as discussed in Customer Engagement, _supra_.

## Technology Solution / Product Development

#### Summary.

We provide a multi-operating system application that supports literary work product creation and collaboration based on a JavaScript (JS) codebase. Several backend capabilities will leverage native Amazon Web Service (AWS) cloud functions that provide on-demand capabilities. Machine learning and performance analytics are provided through Amazon SageMaker using PyTorch and GraphQL as Software-as-a-Service (SaaS) within the AWS ecosystem of services.

Our service is comprised of the eight components listed below. Each component provides value to the customer by providing a quality user experience and a one-stop interface for developing a creative project from any stage of the production process through to publication.

#### Composer (JavaScript Front End).

The user interface (UI) is a cross-platform application written in Node.JS, leveraging React, Redux, and other related libraries. The web application provides a single code base for the other platforms written entirely in JavaScript. We provide cross-platform support for mobile (specifically Android and iOS) devices via React Native. We provide desktop support via Electron. In addition, utilizing an integrated plugin to Microsoft Word will provide support to all the development spaces for authors and editors alike.

This UI provides a rich-text editor that can be used for composing, editing, and commenting on the book project, leveraging UTF-8 for multi-language support with multiple users able to collaborate in real time. Author/editor interactions are managed on platform, with active-push notifications. Editor-availability calendar is managed in the composer.

#### Matchmaker (AWS).

The &quot;Matchmaker&quot; leverages predictive analytics (below) to help anticipate when an author needs to seek out an editor. It offers the author a set of editors identified by the audience and genre they edit for, the type of editing they provide, and their expected availability. This leverages AWS Lambda serverless Functions-as-a-Service (FaaS) and Docker containerization, and is written in a Python codebase. The UI for this app will be equivalent to a Gig-search marketplace or Tinder's swipe-right-or-left interface.

#### Data Store (AWS).

AWS AppSync will be used to implement GraphQL as a query language that writes queries in an object structure over the standard text string. This will greatly reduce the complexity of normal SQL queries between the front end and backend, which will mean lower direct costs to run API calls on AWS. As AppSync will be used as our API to handle requests from our users and retrieve appropriate data, AWS DynamoDB will be used to support the database services. DynamoDB is a serverless, NoSQL database service on AWS that will auto-scale on its own and will easily integrate with AppSync. To support the &quot;Matchmaker&quot; machine learning model, AWS Elastic Container Service (ECS) will be used as the compute resource for the integrated service offerings of Amazon SageMaker. This will ingest the analysis and supporting data for testing, training, testing, and bias/accuracy analysis to improve the machine learning algorithm. With ECS, we will be using Docker as the container image repository as it is already fully integrated into the ECS services. All customer proprietary data will be encrypted with 256-bit Advanced Encryption Standard (AES) symmetric encryption with private keys being managed through AWS Secrets Manager key-paired through a user-only access/egress account policy. This provides authors with a secure workspace for their projects while also allowing them granular access-control rights to the intellectual property to share with editors and the community at large.

#### Exporter (AWS).

The exporter converts the stored work into publication-ready formats (PDF, EPUB, DOCX, RTF) and stores it on the author's selected cloud storage (Dropbox, iCloud, Google Drive, OneDrive, Box, S3). This conversion leverages Pandoc and LaTeX, with Lambda and Docker / Kubernetes orchestration for the processing container.

#### Importer (AWS).

The importer converts uploaded RTF or DOCX into our proprietary format for storage. The process leverages Pandoc and Docker / Kubernetes for processing. We virus-scan these uploaded documents. As a milestone event, we plan to implement and support a voice-to-text conversion of uploaded MP3/4 and WAV using AWS Transcribe to provide convenience for self-publishers to record thoughts and storytelling. Inherently, this will also assist impaired users with any difficulties they may otherwise encounter by self-publishing through standard means of writing and/or typing their work. Additional support for this service includes Amazon Textract (Text-Recognition), Amazon Translate (Language Translation), and Amazon Polly (Text-to-Speech).

#### Account Management (AWS).

User accounts will largely be managed by AWS Cognito, a service that provides identity management and access control to our application. Account creation, user/group management, MFA, device management, password policies, and more will be managed through this service to provide layered security and basic account management to our users. Permissions/Rights will be managed in combination with a database table and AWS Cognito groups. This will allow editors and authors to have transparently different permissions and access to the same resources.

Cognito integrates with iOS, Android, Web, and desktop applications without modification. Cognito will help the user to set these permissions based on their Verkilo subscription (time until expired, active/expired, etc.).

#### Notification (AWS).

To automate notifications to our users, as well as to administrators on system-level events and monitoring, we're implementing AWS' Simple Notification Service (SNS) in combination with AWS' Simple Email Service (SES). SNS/SES is easily integrated into many of the other services AWS offers, including Cognito. This will allow automated email messages to be sent to users for account-creation directions, resetting passwords, and subscription-renewal messages based on expiring subscriptions. These services will also assist in security event information management, automated incident response and recovery, and other logging/monitoring needs for security-related capabilities implemented into our platform.

#### Predictive Analytics / Machine Learning (AWS).

The data collected from editors and authors will include their schedule, genre and audience preferences, and experience, which will serve as inputs for the machine learning model. The model will then begin to match similarities and &quot;chance of matching&quot; between the authors and editors, which will serve as the output.

The data used to train the &quot;Matchmaker&quot; machine learning model will be derived from data initially collected after Verkilo's release and until it is implemented into the production environment. The data used to train the &quot;Matchmaker&quot; will be a random 80% of the collected data, and the test/validation data set will comprise the remaining 20%.

We will use Amazon's SageMaker Studio services to process over fifty (50) industry-leading, optimized, ML-based models utilizing the top three ML platforms (TensorFlow, PyTorch, and Apache MXNet), which are the industry preferred frameworks for text-based input, linear regression, reinforcement, and sentiment training. SageMaker Notebook, Experiment, and Debugger will be directly integrated into AWS' machine learning services, which will allow quick implementation and delivery of our &quot;Matchmaker&quot; model and allow for a pipeline of additional data analytics and derivations of platform service metrics.

## Product Roadmap / Development Path

Verkilo leverages a platform business model by bringing two different market segments together. Our roadmap focuses on attracting both segments to the platform with the goal of generating revenue principally via the editor segment.

**Phase 1 - Composer** involves building the composer capabilities and building out the infrastructure. During this phase, we will be focusing more on the author than the editor to start adding editable data to the platform. Early adopters will receive concierge scheduling by the team while we build out the automated matchmaking & scheduling.

**Phase 2 - Matchmaker** involves delivering the automated matchmaking capability. We pilot the capability initially, replacing the concierge scheduling as we gain confidence in the automation's ability to schedule reliably.

**Phase 3 - Scale** expands the offering to a larger audience.

**Phase 4 – Exit** involves seeking acquisition by Amazon.

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
