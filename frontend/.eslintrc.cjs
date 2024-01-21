module.exports = {
    root: true,
    env: {
        node: true,
    },
    extends: ["plugin:vue/vue3-essential", "eslint:recommended", "@vue/typescript/recommended"],
    parserOptions: {
        ecmaVersion: 2020,
    },
    rules: {
        "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
        "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
        "vue/no-deprecated-slot-attribute": "off",
        "@typescript-eslint/no-explicit-any": "off",

        "vue/padding-line-between-blocks": ["error", "always"],

        //* handled by prettier
        // semi: ["error", "never"],
        // quotes: ["warn", "double"],
        // indent: ["warn", 4, { SwitchCase: 1 }],
        // "linebreak-style": ["error", "unix"],
        // "prefer-const": "warn",
        // "no-multiple-empty-lines": "error",
        // "no-unexpected-multiline": "error",
        // "comma-dangle": ["error", "always-multiline"],
        // "space-before-function-paren": ["error", "never"],
        // "spaced-comment": ["error", "always"],
        // "comma-spacing": ["error", { before: false, after: true }],
        // "no-spaced-func": "error",
        // "keyword-spacing": "error",
        // "object-curly-spacing": ["error", "always"],
        // "array-bracket-spacing": ["error", "never"],
        // "space-infix-ops": "error",
        // "no-unreachable": "error",
        // "no-redeclare": "error",
        // "no-empty": "error",
        // "no-eval": "error",
        // "no-var": "error",
        // "no-shadow": "error",
        // "eqeqeq": ["error", "always"],
        // "curly": ["error", "all"],
    },
}
