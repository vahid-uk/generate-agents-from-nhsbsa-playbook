# Licensing software or code - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-licences/

## Source content

## Contents

- Applying the Apache 2 Licence Each repository should include a licence file Update the copyright notice Add licence in project descriptors

- Each repository should include a licence file

- Update the copyright notice

- Add licence in project descriptors

- OGL v3

# Licensing software or code

Everything we produce or use, whether open or closed, should have an appropriate licence applied (as indicated by the service manual ). Without a licence, others (even within the NHSBSA) have no way of knowing for sure if they can use it, or how.

At the NHSBSA, we use the Apache 2 Licence .

## Applying the Apache 2 Licence

### Each repository should include a licence file

This should be called LICENCE or LICENCE.md . “License” is the U.S. English spelling and should not be used. Gitlab and GitHub will still show licence details for the British English spelling.

Make sure the licence content is included in full, including the title “APACHE LICENSE, VERSION 2.0”, so that readers are quickly able to see which licence is being used.

### Update the copyright notice

The copyright notice is held in the LICENCE file. There is no need to add it to any other source file.

The copyright is Crown Copyright. We put “NHS Business Services Authority” in brackets.

The year should be the year the code was first published. Where the code is updated with significant changes, the year can be shown as a period from first to most recent update (e.g. 2015-2017). Do not update the date range when no significant changes have been made.

```text
Copyright 2022 Crown Copyright (NHS Business Services Authority)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

### Add licence in project descriptors

Many build tools rely on project descriptors to provide machine readable information about a component. E.g. Maven uses the pom.xml file.

Add licence information to the project descriptors.

> Note that NPM uses the SPDX licence classifier for Apache 2 .

Note that NPM uses the SPDX licence classifier for Apache 2 .

- Maven

- NPM

```text
<
project
xmlns
=
"
http://maven.apache.org/POM/4.0.0
"
xmlns:
xsi
=
"
http://www.w3.org/2001/XMLSchema-instance
"
xsi:
schemaLocation
=
"
http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd
"
>
...
<
licenses
>
<
license
>
<
name
>
The Apache Software License, Version 2.0
</
name
>
<
url
>
http://www.apache.org/licenses/LICENSE-2.0.txt
</
url
>
<
distribution
>
repo
</
distribution
>
</
license
>
</
licenses
>
...
</
project
>
```

```text
{
...
"license"
:
"Apache-2.0"
...
}
```

## OGL v3

We use Open Government Licence v3 for our published content. User interfaces need a link to the OGL V3 licence agreement in the footer.

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 6 May 2023

Last reviewed: 6 May 2023

Next review due: 6 May 2024
