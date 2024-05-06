import { useState } from "react";
function SenderForm() {

    // sending the form to the backend
    const createUser = async () => {
        const username = document.getElementsByName("username")[0].value;
        const data = await fetch("http://localhost:5000", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(username)
        })

        if (data.ok) {
            console.log("its ok")
        }

    };


    const [showLogin, setLogin] = useState(false);
    // const [userName, setUserName] = useState("");

    const handleLogin = (e) => {
        if (e) {
            return (<>
                <div className="d-inline-flex gap-3 m-2 form-floating">
                    <div className="input-group mb-3">
                        <label htmlFor="code_label" className="">******</label>
                    </div>
                </div>

                <p className="fs-6 fw-light">copy secure code and send it to the Recevier</p>

                <div className="form-floating mb-3">
                    <button type="button" className="btn btn-success mx-auto">Join Chat</button>
                    {/* <p>{userName || 'no usrname'}</p> */}

                </div>

            </>)
        }
        else {
            return (
                <>
                    <div className="d-inline-flex form-floating mb-3">
                        <input type="text" className="form-control" id="floatingInput" placeholder="..." name="username" />
                        <label htmlFor="floatingInput">Your Name</label>
                        <span className="input-group-text">
                            <button type="submit" onClick={() => {

                                createUser()

                                setLogin(true)



                            }} className="btn btn-outline-warning" >generate code</button>
                        </span>



                    </div>


                </>
            );
        }
    };


    return (
        <>
            <div className="sender-class ">

                <form action="" method="POST">
                    {handleLogin(showLogin)}
                </form>

            </div>



        </>
    );
}

export default SenderForm


