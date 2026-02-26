const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export async function fetchItems() {
    const res = await fetch(`${API_BASE_URL}/items/`);

    if (!res.ok){
        throw new Error('Failed to fetch products');
    }

    return res.json();
}