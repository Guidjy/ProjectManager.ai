const apiBaseUrl = import.meta.env.VITE_API_BASE;

export function login(username, password) {
  console.log('form submitted');
  console.log(`${username} ${password}`);
  console.log(apiBaseUrl);
}