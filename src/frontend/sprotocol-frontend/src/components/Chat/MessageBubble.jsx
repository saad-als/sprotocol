import '../../styles/message-style.css';
function MessageBubble() {
    return (
        <>

            <div className='container-fluid p-3 mt-4 '>

                <div className="card container-md mt-5 border-warning dotted-border position-relative">
                    <div className="card-body">

                        <div className="d-flex flex-row justify-content-start mb-4">
                            <div className=" ms-3">
                                <p className="small mb-0">
                                    Hello and thank you for visiting MDBootstrap. Please click the video
                                    below.
                                    <span className='position-absolute top-0 start-0 translate-middle badge bg-warning '>
                                        sender
                                    </span>
                                </p>
                            </div>
                        </div>


                    </div>

                </div>




                <div className="card container-md mt-5 border-success dotted-border position-relative">
                    <div className="card-body">

                        <div className="d-flex flex-row justify-content-end mb-4">
                            <div className=" ms-3">
                                <p className="small mb-0">
                                    Hello and thank you for visiting MDBootstrap. Please click the video
                                    below.
                                    <span className='position-absolute top-0 start-100 translate-middle badge bg-success '>
                                        recevier
                                    </span>
                                </p>
                            </div>
                        </div>


                    </div>

                </div>
            </div>
        </>
    );

}

export default MessageBubble