import CreativeEditorSDK from '@cesdk/cesdk-js';

const status = document.getElementById('status');
const log = (message) => { status.textContent = message; console.info('[BOSS CESDK]', message); };

try {
  const editor = await CreativeEditorSDK.create('#cesdk_container', {
    // Evaluation mode; exported files may contain IMG.LY watermarks.
    // No license key or protected material is stored in this experiment.
    baseURL: `https://cdn.img.ly/packages/imgly/cesdk-js/${CreativeEditorSDK.version}/assets`,
  });
  editor.ui.setTheme('light');
  await editor.createDesignScene();
  log(`CE.SDK initialized; version=${CreativeEditorSDK.version}; blank editable scene created. Export tests require human operator.`);
  // Test harness only: developer console access for manual export/scene inspection.
  window.bossCesdkTest = { editor, version: CreativeEditorSDK.version };
} catch (error) {
  log(`BLOCKED: CE.SDK initialization failed: ${String(error)}`);
  throw error;
}
