# Lockstead — iPhone app access control

Lockstead helps control which apps can be opened on an iPhone or iPad, using Apple’s Screen Time authorization. Use a six-digit PIN, optional Face ID, temporary access and a daily unlock window.

[Official website](https://materialofair.github.io/lockstead-site/) · [中文官网](https://materialofair.github.io/lockstead-site/zh/) · [Download on the App Store](https://apps.apple.com/app/id6791830193)

## What it does

- Block opening selected apps on your own device after Screen Time authorization.
- Start with one app in the free version.
- Optional VIP: multiple apps, advanced rules, Guest Mode, app-removal controls and appearance options, subject to the current release.
- VIP offers monthly, yearly and lifetime purchase options. See your regional App Store for current prices.
- Requires iOS or iPadOS 17.0 or later.

Lockstead does not encrypt other apps’ content or promise to hide notifications or app icons. iOS background scheduling can affect relocking timing; verify the behavior on your device. Apple handles purchases and restoration over the network.

## Guides

- [How to lock apps on iPhone](https://materialofair.github.io/lockstead-site/guides/lock-apps-iphone/)
- [Guest access when lending your phone](https://materialofair.github.io/lockstead-site/guides/guest-mode-iphone/)
- [Temporary app access](https://materialofair.github.io/lockstead-site/guides/temporary-app-access/)
- [Verified product facts](https://materialofair.github.io/lockstead-site/product/)

## 中文介绍

Lockstead 是 iPhone / iPad 应用访问控制工具，通过 Apple 屏幕使用时间授权限制所选应用的打开。免费版支持一个应用；VIP 提供更多应用与高级规则，含月订阅、年订阅及终身购买选项。

它控制应用访问，不会加密其他应用的数据，也不承诺隐藏图标或通知。设置后请在自己的设备上检查实际锁定与恢复行为。

[中文使用指南与产品资料](https://materialofair.github.io/lockstead-site/zh/product/)

## Support and privacy

[Support](https://materialofair.github.io/lockstead-site/support.html) · [Privacy policy](https://materialofair.github.io/lockstead-site/privacy.html) · [Report an issue](https://github.com/materialofair/lockstead-site/issues)

Issues are public. Do not include passwords, personal content or purchase receipts.

## About this repository

This is the public website and support repository. It does not contain the private application source code.

Edit `site-content.json`, then run `python3 scripts/build-site.py` and `python3 scripts/check-site.py`. GitHub Pages serves the root of this repository. The existing privacy page is preserved. Product facts reviewed on 2026-09-27.
