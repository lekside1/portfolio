# portfolio

This is developed with Vue 3 in Vite.

Click to see live website [Portfolio](https://lekside1.github.io/portfolio/)

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Deploy to github pages
### Manual method
- On remote repository, delete branch "gh-pages"
- In local repository, run commands: 
  - `npm run build`
  - `git add dist -f`
  - `git commit -m "update dist folder"`
  - `git subtree push --prefix dist origin gh-pages`

### Automatic method using npm package "gh-pages"
- Run command `npm run deploy`
- This will cause the `predeploy` and `deploy` scripts defined in package.json to run
- It will take the latest /dist folder push it into the gh-pages branch