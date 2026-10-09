// Recovery evidence is separate from creative approval.
// Do not populate Slides 01/06 from the conflicting 01–03 candidate.
export const slides = [
  { id: '01', title: '[UNKNOWN]', metadata: '[UNKNOWN]', approval: '[UNKNOWN]', layout: 'unresolved' },
  {
    id: '02',
    title: "The Problem Isn't Networking",
    metadata: 'SYSTEM 7 / H-EP01-002',
    approval: '[UNKNOWN]',
    layout: 'diagnostic-comparison',
    comparison: [
      { heading: 'Network-Driven Opportunity', steps: ['Recruit', 'Sell', 'Expand the network'], outcome: 'Growth through distribution' },
      { heading: 'Capability Commerce', steps: ['Learn', 'Build', 'Verify, Deploy, Support'], outcome: 'Value through delivered work' },
    ],
    sidebarHeading: 'OPERATIONAL DISTINCTION',
    sidebar: [
      "Networking itself isn't the problem. Building professional relationships, sharing knowledge, collaborating, and referring customers are legitimate activities.",
      'The difference is what the network exists to produce. In BOSS, a practitioner network coordinates expertise and projects, not recruitment commissions.',
    ],
  },
  { id: '06', title: '[UNKNOWN]', metadata: '[UNKNOWN]', approval: '[UNKNOWN]', layout: 'unresolved' },
];

export const brand = {
  // Supply the original verified asset; never redraw or substitute a logo.
  logoSrc: null,
  logoAlt: 'bioscillate — Operating System by Seven',
};
