module.exports = {
    root: true,
    env: {
        node: true,
    },
    extends: [
        "plugin:vue/vue3-essential",
        "eslint:recommended",
        "@vue/typescript/recommended",
    ],
    parserOptions: {
        ecmaVersion: 2020,
    },
    rules: {
        "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
        "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
        "vue/no-deprecated-slot-attribute": "off",
        "@typescript-eslint/no-explicit-any": "off",
        semi: ["error", "never"],
        quotes: ["warn", "double"],
        indent: ["warn", 4, { SwitchCase: 1 }],
        "linebreak-style": ["error", "unix"],
        "prefer-const": "warn",
    },
}
