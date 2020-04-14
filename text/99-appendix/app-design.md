## Application UI Design

![React Stack for Uniform Cross-Platform Experience](./media/react-crossplatform.png)

Verkilo uses JavaScript, React, ReactNative and ElectronJs for its User Interface code base. This helps us give our user community a consistent user experience and feature set without complicating our code base.

* **ElectronJs** (or Electron) allows organizations to build cross-platform desktop applications. The features and experience enjoyed by Windows and OSX users are the same. Electron was developed by GitHub, now a Microsoft subsidiary. As of this writing, Electron is used by well-known commercial applications including Slack and Discord. [@ElectronBuildCrossplatform] Visual Studio Code, an open source code editor developed by Microsoft and uses Electron, boasted over 2.6 million active users in 2017. [@VisualStudioCode]
* **ReactNative** is a Javascript framework for building native apps using React. This allows Verkilo to provide a consistent mobile user experience whether the user is on Android or MacOS. React Native is great for mobile apps. It provides a slick, smooth and responsive user interface, while significantly reducing load time. It is much faster and cheaper to build apps in React Native as opposed to building native ones, without compromising on quality and functionality. It abstracts the development from the native elements employed. [@ReactNativeFramework] As of 2020, major users of ReactNative include: Skype, Discord, Tesla, Shopify, and Bloomberg. [@StateReactNative] We would prefer to use ReactNative instead of ElectronJs for the desktop UI, but it is less mature in its desktop offerings. Its strength is providing a consistent mobile UI experience.
* **React** is a JavaScript library for building user interface originally developed by Facebook and now maintained by Facebook OpenSource. [@ReactJavaScriptLibrary] It is the foundation for ReactNative, and primary provider of web-interface applications such as Facebook.

![Verkilo Mockup of Editor View (Light / Dark modes)](./media/verkilo-ui-dark-lite.png)

Verkilo's user interface mirrors interfaces used by common content editors such as Visual Studio Code, Scrivener and Word. The mockup figure shows an early prototype example of a working editor for a book comprising multiple documents (sections). The interface will allow authors and editors ready access to key features such as the composer, exporter, and matchmaking scheduler. Our early focus is on major features that delight our user community and provide a clean, minimal interface to reduce distractions.
