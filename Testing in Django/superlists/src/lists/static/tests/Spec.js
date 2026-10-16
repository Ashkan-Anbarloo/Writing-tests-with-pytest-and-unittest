// describe('Player', function() {
//   let player;
//   let song;

//   beforeEach(function() {
//     player = new Player();
//     song = new Song();
//   });

//   it('should be able to play a Song', function() {
//     player.play(song);
//     expect(player.currentlyPlayingSong).toEqual(song);

//     // demonstrates use of custom matcher
//     expect(player).toBePlaying(song);
//   });

//   describe('when song has been paused', function() {
//     beforeEach(function() {
//       player.play(song);
//       player.pause();
//     });

//     it('should indicate that the song is currently paused', function() {
//       expect(player.isPlaying).toBeFalsy();

//       // demonstrates use of 'not' with a custom matcher
//       expect(player).not.toBePlaying(song);
//     });

//     it('should be possible to resume', function() {
//       player.resume();
//       expect(player.isPlaying).toBeTruthy();
//       expect(player.currentlyPlayingSong).toEqual(song);
//     });
//   });

//   // demonstrates use of spies to intercept and test method calls
//   it('tells the current song if the user has made it a favorite', function() {
//     spyOn(song, 'persistFavoriteStatus');

//     player.play(song);
//     player.makeFavorite();

//     expect(song.persistFavoriteStatus).toHaveBeenCalledWith(true);
//   });

//   //demonstrates use of expected exceptions
//   describe('#resume', function() {
//     it('should throw an exception if song is already playing', function() {
//       player.play(song);

//       expect(function() {
//         player.resume();
//       }).toThrowError('song is already playing');
//     });
//   });
// });


describe("Superlists JavaScript", () => {  
  it("should have working maths", () => {  
    expect(1 + 1).toEqual(2);  
  });

  // it("should have working maths", () => {
  //   expect(1 + 1).toEqual(3);
  // });
});

console.log("Spec.js loading");
describe("Superlists JavaScript", () => {
const inputId = "id_text";  
const errorClass = "invalid-feedback";  
const inputSelector = `#${inputId}`;  
const errorSelector = `.${errorClass}`;  
let testDiv;
let textInput;  
let errorMsg;  
beforeEach(() => {
  console.log("beforeEach");
  testDiv = document.createElement("div");
  testDiv.innerHTML = `
        <form>
          <input
            id="${inputId}"  
            name="text"
            class="form-control form-control-lg is-invalid"
            placeholder="Enter a to-do item"
            value="Value as submitted"
            aria-describedby="id_text_feedback"
            required
          />
          <div id="id_text_feedback" class="${errorClass}">An error message</div>  
        </form>
      `;
  document.body.appendChild(testDiv);
  textInput = document.querySelector(inputSelector);  
  errorMsg = document.querySelector(errorSelector);  
  });

  afterEach(() => {  
    testDiv.remove();
  });

  it("should have a useful html fixture", () => {
    expect(errorMsg.checkVisibility()).toBe(true);
  });
  it("should hide error message on input", () => {
    initialize(inputSelector);
    textInput.dispatchEvent(new InputEvent("input"));
    expect(errorMsg.checkVisibility()).toBe(false);
  });
  it("should not hide error message before event is fired", () => {
    initialize(inputSelector);
    expect(errorMsg.checkVisibility()).toBe(true);
  });
});