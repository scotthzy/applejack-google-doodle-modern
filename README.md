# Applejack Google Doodle — Modern Google

An unofficial, non-commercial compatibility port of the old Userstyles.org style **“Applejack is the best pony Doodle”** for the modern Google home page.

This repository is not a GitHub fork of the Userstyles archive. It is a standalone maintenance port containing rewritten compatibility CSS.

## Install

1. Install the [Stylus browser extension](https://github.com/openstyles/stylus).
2. Open [`applejack-google-doodle.user.css`](./applejack-google-doodle.user.css) on GitHub.
3. Click **Raw**. Stylus should offer to install the UserCSS file.
4. Visit a supported Google home page and reload it.

Supported domains:

- `google.com`
- `google.com.hk`
- `google.com.tw`
- `google.cn`

To support another Google domain, add another `domain("...")` entry to the `@-moz-document` rule.

## What changed

The original 2014 style relied on Google selectors that no longer exist, including `#hplogo`, `#gbqlw`, `#gbql`, and `#gbqfw`. This port targets the current home-page logo row and replaces insecure HTTP image loading with an HTTPS archive reference.

The archived image is not copied into this repository. The style references the archived preview remotely and crops the original 540 × 220 doodle region with CSS.

## Original work and attribution

- Original style: [Applejack is the best pony Doodle](https://userstyles.org/styles/107733)
- Original style author: **Axelerre**
- Archive metadata: [uso-archive/data — style 107733](https://github.com/uso-archive/data/blob/flomaster/data/styles/107733.json)
- Archived preview: [107733-0.webp](https://raw.githubusercontent.com/uso-archive/data/flomaster/data/screenshots/107733-0.webp)

See [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md) for the rights and attribution notice.

## Disclaimer

This is an unofficial fan-made project. It is not affiliated with or endorsed by Hasbro, Google, Userstyles.org, the original style author, or the original artwork creator.

Applejack, My Little Pony, Google, and related names, characters, artwork, and marks belong to their respective owners.

## License

The newly written compatibility code in this repository is available under the [MIT License](./LICENSE).

The license does **not** apply to the remotely referenced artwork, the Applejack character, third-party marks, the original Userstyles submission, or material listed in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

## Validation

Run:

```bash
python3 scripts/validate.py
```

GitHub Actions runs the same validation on pushes and pull requests.

---

## 中文说明

这是旧版 Userstyles 样式“Applejack is the best pony Doodle”的非官方、非商业兼容移植版。

仓库只对现代 Google 首页结构进行 CSS 适配，不提交图片文件或 Base64 图片。图片通过 HTTPS 引用公开归档预览，并用 CSS 裁出原来的 540 × 220 图案区域。

MIT 许可证只覆盖新编写的兼容代码，不覆盖第三方图片、角色、商标或原始 Userstyles 内容。
