## [2.0.1](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/2.0.0...2.0.1) (2023-02-22)


### Bug Fixes

* use refresh_token only for grant password_credentials ([3224a1f](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/3224a1f4b33ed0532038ac9b74ff9d74cc969ab7))


### Chores

* **deps:** update dependency playwright to v1.24.0 ([1a70ab4](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/1a70ab46b3f37cfb73aefe8a7d4de97dfeabec60))
* **deps:** update dependency requests to v2.28.1 ([2c625b4](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/2c625b48057a92e37d01b85e34f24e920dc5b226))
* **deps:** update dependency selenium to v4.3.0 ([6d4242a](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/6d4242a0d2002acf01c5b87eed493ecfa4863a89))
* **deps:** update dependency veepee/vptech/ci-cd/markdown-lint to v1.2.1 ([47fbc04](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/47fbc048fc87b55400a446ca2590b156232cc204))

# [2.0.0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.8.0...2.0.0) (2022-07-05)


### Bug Fixes

* **playwright version:** put playwright version ([81b021e](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/81b021e50d4645ef33ed72fd8ee184edf34660bb))
* **playwright:** change playwright version ([5dc312d](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/5dc312d0423234c02249c9456d25196914e0102f))
* **playwright:** change playwright vesion ([e478180](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/e4781804adbd6c67733aac8a2c62f2458b902760))
* **pylint configuration:** change python linter ([e0c676e](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/e0c676e0dfb3b791bad4ab633fb45b84dd20b648))
* **pylint version:** add version to pylint ([87ffdf2](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/87ffdf2db36e1bc4e3d3a6df6794508f84b0a3e2))


### Features

* **ui driver:** implement installation playwright and rework installation selenium webdriver ([047c225](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/047c225676069404c00c2cdc40efddf7cd63cdd3))


### BREAKING CHANGES

* **ui driver:** Implement method to instantiate playwright

# [1.8.0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.7.2...1.8.0) (2022-05-25)


### Features

* **response_message:** improve truncate ([38133d3](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/38133d3d7d92e1854d6fed14e002a76df4134a61))

## [1.7.2](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.7.1...1.7.2) (2022-05-09)


### Bug Fixes

* **response_message:** decode error when it is not bytes ([c0f1c15](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/c0f1c15530528d9aee1a8a598bb760ca3e21944c))

## [1.7.1](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.7.0...1.7.1) (2022-05-04)


### Bug Fixes

* **doc:** update doc and version ([91bce5a](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/91bce5a2dd1f7632f45dfab0ad37c311207c9e5f))


### Chores

* **deps:** update dependency veepee/vptech/sre/iac/ci-cd/python-build to v2.4.1 ([4c6a5b9](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/4c6a5b9bd4fc137f98467ca0ea0b500406d83a96))

# [1.5.0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.4.1...1.5.0) (2021-06-01)


### Features

* **Mssql:** add autocommit option ([db85361](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/db853617a2bb2798c1aadf423bc1dfd0c3646d4b))

## [1.4.1](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.4.0...1.4.1) (2021-06-01)


### Bug Fixes

* **Mssql:** fix problem return execute ps ([d2a4d6a](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/d2a4d6a523fa1ba846d0251284d85b9de2f40e77))
* **Mssql:** fix pylint ([ba850b3](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/ba850b3da6e59944d185146796dbf60c93c7f75a))

# [1.4.0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.3.1...1.4.0) (2021-05-28)


### Features

* **BaseSql:** rework fetch data with retry process ([7ceffc7](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/7ceffc7aaea47e7ab33d99afde2a9ad2f7bee1a0))

## [1.3.1](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.3.0...1.3.1) (2021-04-20)


### Bug Fixes

* **chrome driver:** remove disable-infobars that is useless ([89c013d](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/89c013d875f65108ac9607781e63266c666f7e22))
* **chrome driver:** replace --disable-dev-shm-using by --disable-dev-shm-usage ([f95afb6](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/f95afb69f27cf6c84590c44b5afd5294579a2054))

# [1.3.0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.2.4...1.3.0) (2021-04-15)


### Features

* **browser:** add edge browser webdriver ([547ce38](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/547ce3867717c5a397bc75af4131aff6263e8783))

## [1.2.4](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.2.3...1.2.4) (2021-04-08)


### Bug Fixes

* **sso:** the audience is not required ([31e2de4](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/31e2de4aaef7fbabe169f76aa7ba1157ca69a89c))

## [1.2.3](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.2.2...1.2.3) (2021-04-08)


### Bug Fixes

* **sftp:** force the variable name in the Connection ([3b029c0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/3b029c0fad155b3dcdc9776f1025f4d063090b01))

## [1.2.2](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.2.1...1.2.2) (2021-04-06)


### Bug Fixes

* **gitlab-ci:** revert psycopg2-binary ([213c497](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/213c49779f3c3b1b2d779b31713948683d81b503))

## [1.2.1](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.2.0...1.2.1) (2021-04-06)


### Bug Fixes

* **gitlab-ci:** fix publish-*:python jobs ([3a6e680](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/3a6e68057afa9bbbb132ff02593b7bd64bb8dc2f))

# [1.2.0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.1.0...1.2.0) (2021-04-06)


### Bug Fixes

* **gitlab-ci:** Failed building wheel for cryptography ([8903501](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/890350163b7937339278fcb0b9219c211ff2cd96))
* **gitlab-ci:** Failed building wheel for cryptography ([d12fa5a](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/d12fa5ac67da9aaddecb08ccfe5e21a504313375))


### Features

* **gitlab-ci:** upgrade the python lint cicd version ([8d181b7](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/8d181b7db645aa9a6c37a8320b6489dea28de3ee))
* **sftp:** add sftp client ([f4dbd2f](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/f4dbd2f5743d15b03accb3bebdfd09ed2bc8ff32))

# [1.1.0](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.0.5...1.1.0) (2021-03-30)


### Features

* **LICENSE:** add license file ([cdf6fa9](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/cdf6fa95348cdc3e1a6bc76b09ae02ef0a6daf79))

## [1.0.5](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.0.4...1.0.5) (2021-03-29)


### Bug Fixes

* **services:** base sql commit error in execute_query ([32dab42](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/32dab42556c2c87d66215973bce85190d356314b))

## [1.0.4](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.0.3...1.0.4) (2021-03-26)


### Bug Fixes

* **services:** base sql dependency ([b193258](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/b19325807f5828b4829d5aa0103c90a44bd4401a))

## [1.0.3](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.0.2...1.0.3) (2021-03-26)


### Bug Fixes

* **services:** add init file ([7f46d6d](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/7f46d6dcbf75cb7fc4892d29f0f1705b9a4bee5b))
* **services:** use abstact class for base sql ([7d5f8a8](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/7d5f8a84d7f300550dcf3e52c41936a22fbf919d))

## [1.0.2](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.0.1...1.0.2) (2021-03-26)


### Bug Fixes

* **requirement:** define package version ([2c2647e](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/2c2647eb67502f92400b7e01f8eff5dc5e2ef17a))

## [1.0.1](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/compare/1.0.0...1.0.1) (2021-03-26)


### Bug Fixes

* **setup:** add long_description_content_type ([6328f1a](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/6328f1a8bd662b638813719c0259f95d597b4b45))

# 1.0.0 (2021-03-26)


### Bug Fixes

* **cicd:** change boolean value ([542806b](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/542806bdac12193c3d812d229a9c6f48f867c838))
* **gitlab-ci:** install pgsql dependencies during the lint ([fcc1227](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/fcc1227afac87669fd994439ebdce4635593b52f))
* **lint:** fix function documentation ([a7e5e70](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/a7e5e70aeb02b61edc4f938d973864cdd1341bbe))
* **lint:** function documentation ([64257e4](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/64257e4e61f8361335ee2861852390fbdfa2ace3))
* **readme:** fix lint ([305f2ca](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/305f2ca4157918108ff27273e143b02dbd92ddbb))


### Features

* **cicd:** add cicd ([b47d18b](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/b47d18b2fe9e6380cd90d33e5c5415c3bbd4430a))
* **project:** initialize ([2845bf1](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/2845bf141b3b6ae4208dde12491c2f749efbff98))
* **renovate:** add renovate file ([5b0b7a3](https://git.vptech.eu/veepee/vptech/qa/quality-toolkit/commit/5b0b7a373c5548abf42d8c8b7b677c76b2603440))
