import React, { useState } from 'react';
import { textToSpeech } from '../helpers/textToSpeech';

const TextToSpeechComponent = () => {
    const [text, setText] = useState('');
    const [audioSrc, setAudioSrc] = useState(null);
    // const VOICE_ID = '9BWtsMINqrJLrRacOk9x'; // Replace with your desired voice ID

    const handleGenerateSpeech = async () => {
        try {
            const audio = await textToSpeech(text);
            // setAudioSrc(audio);
            audio.play(); // Set the audio source for playback
        } catch (error) {
            console.error('Failed to generate speech:', error);
        }
    };

    return (
        <div>
            <textarea 
                value={text} 
                onChange={(e) => setText(e.target.value)} 
                placeholder="Enter text here"
            />
            <button onClick={handleGenerateSpeech} className='bg-white text-black'>Generate Speech</button>
            {audioSrc && <audio controls src={audioSrc} />}
        </div>
    );
};

export default TextToSpeechComponent;