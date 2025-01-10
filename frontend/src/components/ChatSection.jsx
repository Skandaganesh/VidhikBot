import React, { useEffect, useRef, useState } from 'react'
import Input from './Input'
import Response from '../ui/Response'
import ResponseLoader from '../loaders/ResponseLoader';
import SelectionBox from './SelectionBox';

const ChatSection = ({ handleHistory }) => {

  const chatRef = useRef(null);

  const colleges = [
    'Government Polytechnic College, Ajmer',
    'Government Polytechnic College, Jodhpur',
    'Government Polytechnic College, Kota',
  ];

  const selectCollege = (collegeInd) => {
    const message = `I got it, now you can ask me about ${colleges[collegeInd]}`;
    setChats(prev => [...chats.slice(0,1),{ content:message,isUser:false }]);
  }

  const initialChats = [
    {
      content:"Hey Nishant, How can I assist you today? 😊",
      isUser:false
    },
    {
      content:<SelectionBox colleges={colleges} selectCollege={selectCollege} />,
      isUser:false
    }
  ];

  const [chats, setChats] = useState(initialChats);
  const [isBotThinking, setIsBotThinking] = useState(false);
  const [responseInd, setResponseInd] = useState(0);

  const scrollToBottom = () => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  }

  useEffect(() => {
    scrollToBottom();
  },[chats]);

  const getUserInput = (value) => {
    setChats(prev => [...prev,{ content:value,isUser:true }]);
    setIsBotThinking(true);
    setTimeout(() => { getChatBotResponse(value); },2000);
  }

  const getChatBotResponse = (userInput) => {
    const chatBotResponses = [
      "Government Polytechnic College Jodhpur was established in 1958. Initially, diploma certificate courses started at MBM Engineering College Jodhpur in 1951.",
      "The college offers the following 3-year Diploma Courses: Civil Engineering, Electrical Engineering, Electronics & Fiber Optics Engineering, Mechanical Engineering, and Computer Science Engineering.",
      "Yes, hostel facilities are available for both male and female students.",
      "The Boys' Hostel provides 54 rooms, mess facilities, STD/PCO, water coolers, television, and newspapers to create a comfortable academic environment.",
      "There is no college bus facility, but there's common bus available for colleges.",
      "Yes, admission for first year diploma courses is open.",
      "To apply for admission to the first-year diploma courses, you can visit the DTE Admission Portal at this link: https://dteapp.hte.rajasthan.gov.in/dte_admission/admission/index/1.",
      "To apply, visit the admission link, register, fill out the application form, upload required documents, pay the application fee, and submit your application. Be sure to check the portal for updates on your application status.",
      "You're welcome! If you have any more questions in the future or need assistance, feel free to reach out. Have a great day! 😊"
    ];
    
    setIsBotThinking(false);
    setChats(prev => [...prev,{ content:chatBotResponses[responseInd],isUser:false }]);
    setResponseInd(p => p+1);
  }

  const createNewConversation = () => {
    setChats(initialChats);
    handleHistory();
  }

  return (
    <div className='flex-1 flex flex-col relative p-2 bg-violet-50 bg-contain bg-no-repeat bg-center'>
        <div className='flex flex-col gap-2 overflow-y-scroll overflow-x-hidden scroll-smooth pb-14' ref={chatRef}>
            {
              chats.map((response,ind) => <Response key={ind} response={response.content} isUser={response.isUser} />)
            }
            {isBotThinking?<ResponseLoader />:null}
        </div>    
        <div className='flex items-center justify-center absolute bottom-0 right-0 left-0 backdrop-blur-[2px] pb-4 px-2'>
        <Input getUserInput={getUserInput} />
        </div>
        <span className='text-lg text-slate-700 absolute top-0 right-0 flex items-center gap-1 bg-white rounded shadow py-1 px-2' onClick={createNewConversation}><i className="fa-solid fa-pen-to-square"></i><p className='text-sm font-semibold'>New Conversation</p></span>
    </div>
  )
}

export default ChatSection