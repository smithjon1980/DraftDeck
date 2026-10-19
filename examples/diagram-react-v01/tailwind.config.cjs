module.exports = {
  content: ['./src/**/*.{js,jsx}', './index.html'],
  theme: { extend: {
    colors: { 'boss-white': '#FFFFFF', 'boss-ink': '#000000',
      'boss-cyan': '#00BCEB', 'boss-magenta': '#E30074' },
    fontFamily: { display: ['Arial', 'Helvetica', 'sans-serif'],
      label: ['"Courier New"', 'monospace'] },
  }},
  plugins: [],
};
