## Application Infrastructure

Verkilo will use many available services and cloud-based techniques to provide scalable availability and automated infrastructure as code. The diagram below describes our high-level infrastructure architecture. This does not preclude adding additional resources, services, or software to manage our Agile development projects.

![Verkilo Infrastructure Architecture](./media/verkilo-architecture.png)

**High Level Design Principles:**

* AWS Virtual Private Cloud (VPC) network with appropriate Public, Private, and Database Subnets.
* AWS Identify and Access Management (IAM) service for cloud console access for all approved administrators and developers with specific Access Control Lists (ACLs) for each group of users for Least Privilege and Segregation of Duty.
* Initial AWS account compliance will be configured upon creation using AWS SecurityHub to satisfy Center for Internet Security (CIS) version 1.2 standards.
* For payment transactions for processing service fees and editorial transactions, we will apply AWS SecurityHub configurations for monitoring and meeting the Payment Card Industry Security Standards Council’s (PCI-DSS) compliance standard as well.
* Between Verkilo’s connections to systems (EC2) running in our AWS environment, we use OpenVPN servers to manage access into the development and production environments.
* AWS DynamoDB database for User Account controls, credentials, ACLs.
* Stand up frontend webservices for Verkilo primary outreach sites for marketing, forums, blogs, and community tutorials.
* AWS EC2 instances using containerized and serverless Lambda services to process and manage all the Verkilo provided components.
* Verkilo use AWS SageMaker for Machine Learning and its respective Notebooks product to develop tests, bias analysis, and data processing outputs for providing ML-driven results to our customers.
* Other automated security and business tool services will be applied to our product offerings to align with Verkilo’s vision of providing a complete vertical integration of the publishing process. Examples are Textract, Forecast, Transcribe, Polly, etc.
