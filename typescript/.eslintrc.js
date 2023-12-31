module.exports = {
  root: true,
  extends: ['@cv9t/eslint-config/base'],
  ignorePatterns: ['.eslintrc.js', 'jest.config.js'],
  rules: {
    '@typescript-eslint/no-extraneous-class': 'off',
  },
};
