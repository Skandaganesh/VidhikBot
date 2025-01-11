import axios from 'axios';
const textToSpeech = async (inputText, voiceId="9BWtsMINqrJLrRacOk9x") => {
    const API_KEY = "sk_03e77cc88057e66a5f76c2dd7b8f1b0c2ff110a37b480a65"; // Use environment variables instead
    try {
        const response = await axios.post(
            `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`,
            {
                text: inputText,
                voice_settings: {
                    stability: 0,
                    similarity_boost: 0.75
                }
            },
            {
                headers: {
                    'xi-api-key': API_KEY,
                    'Content-Type': 'application/json'
                },
                responseType: 'arraybuffer'
            }
        );

        if (response.status === 200) {
            console.log('Speech generated successfully.');

            // Convert ArrayBuffer to Blob
            const audioBlob = new Blob([response.data], { type: 'audio/mpeg' });

            // Create a URL for the audio blob
            const audioUrl = URL.createObjectURL(audioBlob);

            // Play the audio using the URL
            const audio = new Audio(audioUrl);
//audio.play();

            return audio; // Optionally return the URL for further use
        } else {
            console.error('Unexpected response status:', response.status);
        }
    } catch (error) {
        console.error('Error generating speech:', error.response ? error.response.data : error.message);
        throw error;
    }
};

export { textToSpeech };
