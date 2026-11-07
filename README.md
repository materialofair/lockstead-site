# App Lock: Lockstead for iPhone and iPad

Lockstead restricts selected apps on your own iPhone or iPad using Apple's Screen Time. Choose which apps can open before lending your device, set protection schedules, or temporarily allow access. Protect Lockstead settings with a six-digit PIN and optional Face ID or Touch ID.

[Official website](https://lockstead.siproducers.com/) · [中文官网](https://lockstead.siproducers.com/zh-hans/) · [Download on the App Store](https://apps.apple.com/app/id6791830193) · [Public source snapshot](https://github.com/materialofair/Lockstead-source)

## What it does

- **Free core:** protection for one selected app.
- **Optional VIP:** multi-app management, Guest Mode, advanced rules, app-removal controls, themes and alternate icons.
- **Purchase options:** monthly or yearly auto-renewing subscription, or a one-time lifetime VIP purchase. Check the regional App Store for prices.
- **Requirements:** iOS/iPadOS 17 or later and Screen Time authorization.

## When is Guest Mode useful?

Guest Mode is for a temporary handoff, such as lending your phone for a map or your iPad for reading. Choose supported apps and a duration from 15 minutes to 12 hours. Test an allowed app and a restricted app before handing over the device.

Guest Mode takes priority over normal lock and temporary-access rules. When the session ends, Lockstead reapplies the rules for that time; it does not simply unlock everything. iOS background scheduling can delay changes.

## What are the limits?

Lockstead controls app access. It does not encrypt other apps' files, guarantee hidden icons, suppress notifications, create a separate user account or separate data inside allowed apps. Content inside an allowed app remains accessible. It is not remote device management. Availability and enforcement depend on iOS.

No app account, developer backend, advertising SDK or analytics SDK is required. Protection settings stay on the device; Apple handles purchases and restoration over the network.

## Guides and product facts

- [App lock on iPhone without an app account](https://lockstead.siproducers.com/guides/app-lock-iphone-no-account/)
- [Everyday privacy and lending your phone](https://lockstead.siproducers.com/guides/real-life-privacy/)
- [Product facts](https://lockstead.siproducers.com/product/)
- [Machine-readable product facts](https://lockstead.siproducers.com/product-facts.json)

## 中文介绍

Lockstead 的 App Store 名称是 **App Lock: Lockstead**，是一款 iPhone/iPad 应用访问限制工具。通过 Apple 屏幕使用时间授权，可限制所选应用、设置保护时间表或临时放行；设置入口由六位 PIN 和可选 Face ID/Touch ID 保护。

免费核心支持一个应用。VIP 提供多应用管理、访客模式与高级规则，可选月订阅、年订阅或一次性终身购买。访客模式适用于临时借出自己的手机或平板，不会创建独立用户或隔离获准应用内部的数据。不会加密其他应用文件，也不保证隐藏图标或通知。iOS 调度可能延迟规则恢复，借出设备前请检查实际行为。

## Support, privacy and source

[Support](https://materialofair.github.io/lockstead-site/support.html) · [App Store-linked privacy policy](https://materialofair.github.io/lockstead-site/privacy.html) · [Report an issue](https://github.com/materialofair/lockstead-site/issues)

Issues are public. Do not include passwords, personal content or purchase receipts.

This repository contains the GitHub Pages support site. The current product website is [lockstead.siproducers.com](https://lockstead.siproducers.com/). The application source snapshot is published separately in [Lockstead-source](https://github.com/materialofair/Lockstead-source); source availability does not constitute an independent security audit or establish a byte-for-byte match with the App Store binary.

To maintain the GitHub Pages pages in this repository, edit `site-content.json`, then run `python3 scripts/build-site.py` and `python3 scripts/check-site.py`. Those scripts do not publish the separate product website. The existing privacy page is preserved.

Product descriptions checked against the [public App Store listing](https://apps.apple.com/us/app/app-lock-lockstead/id6791830193), version 1.2.4, on 2026-11-07.
