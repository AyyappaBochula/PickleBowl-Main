// PickleBowl Central API Configuration
export const API_BASE_URL = (import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000').replace(/\/$/, '');
export const API = `${API_BASE_URL}/api`;

export default API;
