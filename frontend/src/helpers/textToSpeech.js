import axios from 'axios';

const textToSpeech = async (inputText, voiceId) => {
    const API_KEY = "sk_03e77cc88057e66a5f76c2dd7b8f1b0c2ff110a37b480a65"; // Store your API key in environment variables

    try {
        const response = await axios.post(
            `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`,
            {
                text: inputText,
                voice_settings: {
                    stability: 0, // Customize as needed
                    similarity_boost: 0.75 // Customize as needed
                }
            },
            {
                headers: {
                    'xi-api-key': API_KEY,
                    'Content-Type': 'application/json'
                }
            }
        );
        console.log('Speech generated:', response.data);
        
        return response.data; // This will contain the audio stream or URL
    } catch (error) {
        console.error('Error generating speech:', error);
        throw error;
    }
};

export { textToSpeech };