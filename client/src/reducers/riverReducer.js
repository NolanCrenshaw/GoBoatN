import {
  SET_RIVERS_START,
  SET_RIVERS_SUCCESS,
  SET_RIVERS_FAILURE,
  SET_ACCESSES_START,
  SET_ACCESSES_SUCCESS,
  SET_ACCESSES_FAILURE,
  CREATE_RIVER_START,
  CREATE_RIVER_SUCCESS,
  CREATE_RIVER_FAILURE,
  UPDATE_RIVER_START,
  UPDATE_RIVER_SUCCESS,
  UPDATE_RIVER_FAILURE,
} from "../actions/riverActions";

const riverReducer = (state = {}, action) => {
  Object.freeze(state);
  let nextState = { ...state };
  switch (action.type) {
    case SET_RIVERS_START:
      nextState.loading = true;
      return nextState;
    case SET_RIVERS_SUCCESS:
      // nextState = action.rivers;
      const raw_rivers = action.rivers;
      const rivers = {};
      for (const river in raw_rivers) {
        const riversID = raw_rivers[river].id;
        rivers[riversID] = raw_rivers[river];
      }
      nextState = rivers;
      nextState.loading = false;
      return nextState;
    case SET_RIVERS_FAILURE:
      nextState.error = action.error;
      nextState.loading = false;
      return nextState;
    case SET_ACCESSES_START:
      nextState.loading = true;
      return nextState;
    case SET_ACCESSES_SUCCESS:
      // ~~ TODO ~~
      console.log(nextState[0].id);
      nextState.loading = false;
      return nextState;
    case SET_ACCESSES_FAILURE:
      nextState.loading = false;
      return nextState;
    case CREATE_RIVER_START:
      nextState.loading = true;
      return nextState;
    case CREATE_RIVER_SUCCESS:
      const newRiver = action.river;
      nextState = { ...nextState, newRiver };
      nextState.loading = false;
      return nextState;
    case CREATE_RIVER_FAILURE:
      nextState.error = action.error;
      nextState.loading = false;
      return nextState;
    case UPDATE_RIVER_START:
      nextState.loading = true;
      return nextState;
    case UPDATE_RIVER_SUCCESS:
      const mappedRivers = Object.values(newState).map((river) => {
        if (river.id === action.river.id) {
          return action.river;
        } else {
          return river;
        }
      });
      nextState = { ...mappedRivers };
      nextState.loading = false;
      return nextState;
    case UPDATE_RIVER_FAILURE:
      nextState.error = action.error;
      nextState.loading = false;
      return nextState;
    default:
      return state;
  }
};

export default riverReducer;
