import axios from 'axios';
// const DEVELOPMENT_API_KEY = 'test_30da4632313e8404c8bdee6917079f96'
const PRODUCTION_API_KEY = 'prod_2cb40a144efbb077d7e37d1f9298c181';

const API = (baseUrl) => ({
  ping: async () => {
    try {
      const response = await axios.post(`${baseUrl}ping`, {
        apiKey: PRODUCTION_API_KEY
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  getNodes: async () => {
    try {
      const response = await axios.post(`${baseUrl}getNodes`, {
        apiKey: PRODUCTION_API_KEY,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  getImportant: async () => {
    try {
      const response = await axios.post(`${baseUrl}getImportant`, {
        apiKey: PRODUCTION_API_KEY,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  internal: async () => {
    try {
      const response = await axios.post(`${baseUrl}internal`, {
        apiKey: PRODUCTION_API_KEY,
      });
      throw new Error('Not implemented.');
    } catch (error) {
      throw error;
    }
  },
});

export { API };
