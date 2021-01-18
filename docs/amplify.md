# AWS Amplify

## Prerequisites

Please install AWS Amplify CLI : `npm install -g @aws-amplify/cli`

## Configuration

You must run following commands  in `www` folder :

- `amplify configure`
- `amplify init`
  - What javascript framework are you using: `vue`
  - Source Directory Path:  `src`
  - Distribution Directory Path: `dist`
  - Build Command:  `npm run-script build`
  - Start Command: `npm run-script serve`
  - Do you want to use an AWS profile? `Yes`
  - Please choose the profile you want to use: `amplify`
- `amplify add auth`
  - Do you want to use the default authentication and security configuration? `Default configuration`
  - How do you want users to be able to sign in? `Email`
  - Do you want to configure advanced settings? `No, I am done.`
- `amplify hosting add`
  - Select the plugin module to execute `Hosting with Amplify Console (Managed hosting with custom domains, Continuous deployment)`
  - Choose a type Continuous deployment `(Git-based deployments)`
- `amplify push`
