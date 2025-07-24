import React from 'react';

const ChatLoading = () => {
    return (
    <div className="flex items-center justify-center h-16 w-16">
        <div className={`h-10 w-10 rounded-full border-4 border-t-4 border-gray-300 border-t-indigo-500 animate-spin`} role="status" aria-label="Loading…" />
    </div>
    )
};

export default ChatLoading;