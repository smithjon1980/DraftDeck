import type { E2EConfig } from 'e2e';
import { web } from '@e2e-dev/web';
export default {
  tests: 'tests/editorial-gate.e2e.ts',
  targets: [{ name: 'chromium', engine: web({ viewport: { width: 1920, height: 1080 } }), app: { url: 'http://127.0.0.1:8765', command: { executable: 'python3', args: ['-m','http.server','8765','--directory','fixture'], reuseExisting: true } } }],
  workers: 1,
  reporters: ['list','junit'],
} satisfies E2EConfig;
