import registry from '../../../design-system/registries/draftdeck_standards_registry_v1.json';
export const design_tokens = registry.design_tokens;
export const contracts = registry.component_contracts;
export const registryVersion = registry.registry_version;
export function requireContract(id: string) {
  const contract = contracts.find(c => c.element_id === id);
  if (!contract) throw new Error('Missing DraftDeck component contract: ' + id);
  return contract;
}
export function assertExactTitle(content: string) {
  requireContract('EP01.S01.TEXT.TITLE');
  if (content !== 'YOU ALREADY MOVE INFORMATION') throw new Error('Approved source copy mismatch: EP01.S01.TEXT.TITLE');
}
