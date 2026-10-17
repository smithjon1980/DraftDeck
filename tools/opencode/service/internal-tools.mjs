import express from 'express';
import path from 'node:path';

export function createInternalTools(root) {
  const router = express.Router();
  router.use((_req, res, next) => {
    res.set('Cache-Control', 'private, no-store');
    res.set('X-Content-Type-Options', 'nosniff');
    res.set('Referrer-Policy', 'same-origin');
    next();
  });
  router.get('/', (_req, res) => res.sendFile(path.join(root, 'tools.html')));
  router.get('/atlas/download', (_req, res) => res.download(path.join(root, 'public/atlas/complete.zip'), 'DraftDeck_Engineering_Atlas_Complete.zip'));
  router.use('/atlas', express.static(path.join(root, 'public/atlas'), { index: 'index.html', dotfiles: 'deny', fallthrough: false, etag: false, cacheControl: false }));
  return router;
}
